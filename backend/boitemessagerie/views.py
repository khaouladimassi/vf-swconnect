from urllib.parse import urljoin
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Messagerie
from rest_framework import status
from .models import CustomUser
from .serializers import MessagerieSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Messagerie.objects.all()
    serializer_class = MessagerieSerializer

class SendMessage(APIView):
    def post(self, request, sender_id, recipient_id):
        try:
            sender = CustomUser.objects.get(id=sender_id)
            recipient = CustomUser.objects.get(id=recipient_id)

            # Create the message data
            data = {
                'sender': sender.id,
                'receiver': recipient.id,
                'body': request.data.get('body'),
                'file':request.data.get('file')
            }
            serializer = MessagerieSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except CustomUser.DoesNotExist:
            return Response({"detail": "Sender or recipient not found."}, status=status.HTTP_404_NOT_FOUND)


    
class DeleteMessage(APIView):
    def delete(self, request, message_id):
        message = get_object_or_404(Messagerie, id=message_id)
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SeenMessage(APIView):
    def put(self, request, user_id):
        try:
            # Find the latest message received by the user from the other user
            latest_message = Messagerie.objects.filter(receiver_id=user_id, seen=False).order_by('-timestamp').first()

            # Mark the message as seen if it exists and sender is the other user
            if latest_message and latest_message.sender_id != user_id:
                latest_message.seen = True
                latest_message.save()
                return Response({"detail": "Latest message from other user marked as seen."}, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "No suitable message found."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from urllib.parse import urljoin
from .models import Messagerie, CustomUser

class GetRecipientOrSender(APIView):
    def get(self, request, user_id):
        try:
            # Fetch distinct user ids where the user_id is either sender or receiver
            sent_messages = Messagerie.objects.filter(sender_id=user_id).values_list('receiver_id', flat=True)
            received_messages = Messagerie.objects.filter(receiver_id=user_id).values_list('sender_id', flat=True)
            distinct_user_ids = set(sent_messages).union(set(received_messages))

            if not distinct_user_ids:
                return Response({"error": "No messages found for this user"}, status=status.HTTP_404_NOT_FOUND)

            recipient_data = []
            
            for other_user_id in distinct_user_ids:
                other_user = CustomUser.objects.get(id=other_user_id)

                data = {
                    "other_user_id": other_user.id,
                    "username": other_user.username,
                    "user_type": other_user.user_type
                }

                if hasattr(other_user, 'etudiant') and other_user.etudiant:
                    data['profile_photo'] = urljoin(request.build_absolute_uri('/')[:-1], other_user.etudiant.profile_photo.url) if other_user.etudiant.profile_photo else None
                    data['etudiant_lastname'] = other_user.etudiant.last_name if other_user.etudiant.last_name else None
                    data['etudiant_firstname'] = other_user.etudiant.first_name if other_user.etudiant.first_name else None
                elif hasattr(other_user, 'entreprise') and other_user.entreprise:
                    data['profile_logo'] = urljoin(request.build_absolute_uri('/')[:-1], other_user.entreprise.profile_logo.url) if other_user.entreprise.profile_logo else None
                    data['entreprise_nom'] = other_user.entreprise.nom if other_user.entreprise.nom else None
                elif hasattr(other_user, 'admin') and other_user.admin:
                    data['profile_photo'] = urljoin(request.build_absolute_uri('/')[:-1], other_user.admin.profile_photo.url) if other_user.admin.profile_photo else None

                # Get the latest message between the sender and receiver
                latest_message = Messagerie.objects.filter(
                    (Q(sender_id=user_id) & Q(receiver_id=other_user.id)) |
                    (Q(sender_id=other_user.id) & Q(receiver_id=user_id))
                ).order_by('-timestamp').first()
                
                if latest_message:
                    data['latest_message_id'] = latest_message.id
                    data['latest_message_body'] = latest_message.body
                    data['time'] = latest_message.timestamp
                    data['latest_message_sender'] = latest_message.sender_id
                    data['latest_message_seen'] = latest_message.seen
                else:
                    data['latest_message_id'] = None
                    data['latest_message_body'] = None
                    data['time'] = None
                    data['latest_message_sender'] = None
                    data['latest_message_seen'] = None

                # Collect all messages between sender and receiver
                messages = Messagerie.objects.filter(
                    (Q(sender_id=user_id) & Q(receiver_id=other_user.id)) |
                    (Q(sender_id=other_user.id) & Q(receiver_id=user_id))
                ).order_by('timestamp')

                message_list = []
                for message in messages:
                    message_data = {
                        'message_body': message.body,
                        'time': message.timestamp,
                        'sender_id': message.sender.id,
                        'sender_username': message.sender.username,
                        'receiver_id': message.receiver.id,
                        'receiver_username': message.receiver.username
                    }
                    message_list.append(message_data)

                data['messages'] = message_list
                recipient_data.append(data)

            return Response(recipient_data, status=status.HTTP_200_OK)
        
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        except Messagerie.DoesNotExist:
            return Response({"error": "Message not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class GetMessagesBetweenUsers(APIView):
    def get(self, request, sender_id, receiver_id):
        sender = get_object_or_404(CustomUser, id=sender_id)
        receiver = get_object_or_404(CustomUser, id=receiver_id)
        messages = Messagerie.objects.filter(
            (Q(sender_id=sender_id) & Q(receiver_id=receiver_id)) |
            (Q(sender_id=receiver_id) & Q(receiver_id=sender_id))
        ).order_by('timestamp')
        messages_data = []
        for message in messages:
            message_info = {
                "sender_id": message.sender.id,
                "sender_username": message.sender.username,
                "receiver_id": message.receiver.id,
                "receiver_username": message.receiver.username,
                "body": message.body,
                "timestamp": message.timestamp
            }
            if message.file:  # Check if file is not null
                message_info["file"] = message.file.url  # Assuming file is a FileField or similar
            messages_data.append(message_info)
        return Response(messages_data, status=status.HTTP_200_OK)

    

