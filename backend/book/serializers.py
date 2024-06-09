from rest_framework import serializers

from entreprise.serializers import EntrepriseSerializer
from offer.serializers import OfferSerializer
from .models import Book

from .models import Book, Offer, Entreprise

class BookSerializer(serializers.ModelSerializer):
    offer_ids = serializers.PrimaryKeyRelatedField(queryset=Offer.objects.all(), many=True, source='offers')
    offers = OfferSerializer(many=True, read_only=True)
    entreprise = EntrepriseSerializer(read_only=True)

    class Meta:
        model = Book
        fields = "__all__"

    def create(self, validated_data):
        offers = validated_data.pop('offers')
        book = Book.objects.create(**validated_data)
        book.offers.set(offers)
        return book












