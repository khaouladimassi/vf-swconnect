<template>
  <router-view></router-view>
  <head>
    <meta charset="UTF-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, maximum-scale=1"
    />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <meta name="msapplication-TileColor" content="#0E0E0E" />
    <meta name="template-color" content="#0E0E0E" />
    <meta name="msapplication-config" content="browserconfig.html" />
    <meta name="description" content="Index page" />
    <meta name="keywords" content="index, page" />
    <meta name="author" content="" />
    <title>Messagerie</title>
    <link
      href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
      rel="stylesheet"
    />
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css"
      rel="stylesheet"
    />
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.1/font/bootstrap-icons.css"
      rel="stylesheet"
    />
    <link
      href="https://cdn.tiny.cloud/1/YOUR_API_KEY/tinymce/5/tinymce.min.js"
      referrerpolicy="origin"
    />
    <link
      rel="shortcut icon"
      type="image/x-icon"
      href="/template/assets/imgs/template/favicon.svg"
    />

    <link
      href="/template/assets/css/plugins/animate.min.css"
      rel="stylesheet"
    />
    <link
      href="/template/assets/css/plugins/magnific-popup.css"
      rel="stylesheet"
    />
    <link
      href="/template/assets/css/plugins/perfect-scrollbar.css"
      rel="stylesheet"
    />
    <link
      href="/template/assets/css/plugins/select2.min.css"
      rel="stylesheet"
    />
    <link
      href="/template/assets/css/plugins/swiper-bundle.min.css"
      rel="stylesheet"
    />

    <link href="/template/assets/css/stylecd4ee.css" rel="stylesheet" />

    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"
    />
  </head>
  <body>
  <navbarEntreprise v-if="userType === 'entreprise'" />
    <navbarEtudiant v-if="userType === 'etudiant'" />
    <navbarAdmin v-if="userType === 'admin'" />
    <div class="chat-app">
      <div class="sidebar">
        <button @click="openNewMessageModal" class="new-message-btn">
            <img src="/template/assets/imgs/template/icons/pencil.svg" alt="new chat"></button>
        <div class="users-list">
          <h2>Dernières Discussions</h2>
          <ul>
            <li v-for="message in messages" :key="message.id" @click="openChat(message.other_user_id)">
              <span v-if="message.user_type=='entreprise'" class="profile"><img :src="message.profile_logo" alt="profile_picture"></span>
              <span v-if="message.user_type==='etudiant'" class="profile"><img :src="message.profile_photo" alt="profile_picture"></span>
              <span v-if="message.user_type==='admin'" class="profile"><img :src="message.profile_photo" alt="profile_picture"></span>
              <div class="container-message">
                <span v-if="message.user_type==='etudiant'"  class="username">{{message.etudiant_firstname}} {{message.etudiant_lastname}}</span>
              <span v-if="message.user_type=='entreprise'"  class="username">{{message.entreprise_nom}}</span>
              <span v-if="message.user_type==='admin'" class="username">{{message.username}}</span>
              <span v-if="message.latest_message_sender === this.currentUserId && message.latest_message_body!==null"  
              class="text-message">{{ message.latest_message_body.slice(0,22) }}..</span>
              <span  v-if="message.latest_message_sender!==this.currentUserId && message.latest_message_seen===false && message.latest_message_body!==null"
              class="text-message"><b class="bold-weight">{{ message.latest_message_body.slice(0,22) }}..</b></span>
              <pre>{{this.currentUserId}}</pre>
              <span  v-if="message.latest_message_sender!==this.currentUserId && message.latest_message_seen===true && message.latest_message_body!==null"
              class="text-message">{{ message.latest_message_body.slice(0,22) }}..</span>


              <span v-if="message.latest_message_sender === this.currentUserId && message.latest_message_body===null"  
              class="text-message">file</span>
              <span  v-if="message.latest_message_sender!==this.currentUserId && message.latest_message_seen===false && message.latest_message_body===null"
              class="text-message"><b class="bold-weight">file</b></span>
              <pre>{{this.currentUserId}}</pre>
              <span  v-if="message.latest_message_sender!==this.currentUserId && message.latest_message_seen===true && message.latest_message_body===null"
              class="text-message">file.pdf</span>
              </div>

              <span class="timestamp">{{ formatTimestamp(message.time) }}</span>
            </li>
          </ul>
        </div>
      </div>
      
      <div class="chat-container">
        <header v-if="activeUser "  class="chat-header">

             <img v-if="activeUser && activeUser.entreprise_details"  :src="this.baseUrl+activeUser.entreprise_details.profile_logo" alt="Profile Logo">
             <img v-if="activeUser && activeUser.etudiant_details"  :src="this.baseUrl+activeUser.etudiant_details.profile_photo" alt="Profile Photo">
             <img v-if="activeUser && activeUser.admin_details"  :src="this.baseUrl+activeUser.admin_details.profile_photo" alt="Profile Photo">
       
          <h6 v-if="activeUser ">{{ this.activeUser ? this.activeUser.username : '...' }}</h6>
        </header>
        <div class="chat-window">
          <div class="messages">
            <div v-for="(chat, index) in chats" :key="index"  :class="messageClasses(chat)" >
              <div v-if="chat.body!==null" class="message-content">{{ chat.body }}</div>
              <div v-if="chat.body===null" class="message-content" style="background-color:#fff">
                <div class="container-file">
                  <img src="/template/assets/imgs/template/icons/file-earmark-pdf (1).svg" alt="file" @click="openFile(chat.file)">
                  <p>File</p>
                </div>
              </div>
              <div class="message-timestamp">{{ formatTimestamp(chat.timestamp) }}</div>
            </div>
          </div>
          <div v-if="!activeUser " class="home-page-chat">
              <div class="card-container">
                <div class="chat-image"> <img src="template/assets/imgs/page/chat.png"></div>
              </div>
              <p v-if="this.userType==='etudiant'">Bienvenue, vous pouvez contacter des entreprises maintenant ! </p>
              <p v-if="this.userType==='entreprise'">Bienvenue, vous pouvez contacter des entreprises maintenant ! </p>
              <p v-if="this.userType==='admin'">Bienvenue, Admin ! </p>
      

            </div>
        </div>
        <footer class="chat-footer" v-if="activeUser">
          <img style="cursor:pointer;" src="/template/assets/imgs/template/icons/paper-clip.svg" alt="paper-clip" @click="openModal">
          <input 
            v-model="newMessage" 
            @keyup.enter="sendMessage" 
            type="text" 
            placeholder="Type a message..." 
            class="chat-input" 
          />
          <button @click="sendMessage" class="send-button">Send</button>
        </footer>
      </div>

      <div v-if="showModal" class="modal">
        <div class="modal-content">
          <span class="close" @click="closeNewMessageModal">&times;</span>
          <h2 class="modal-title">Nouveau message</h2>
          <input
            type="text"
            v-model="newUsername"
            @input="filterUsernames"
            placeholder="Enter username"
            class="username-input"
          />
          <ul v-if="filteredUsernames.length" class="suggestions">
            <li v-for="username in filteredUsernames" :key="username" @click="selectUsername(username)"><span class="name">{{ username }}</span></li>
          </ul>
        </div>
      </div>
      <!-- Modal content -->
<div v-if="isModalOpen" id="myModal" class="modal-2">
<!-- Modal content -->
<div class="modal-content-2">
  <div class="modal-header-2">
    <h2>Drive</h2>
    <span class="close-2" @click="closeModal">&times;</span>
  </div>
  <div class="modal-body-2">
   <div v-for="file in files" :key="file.id" class="container-cards-modal" >
    
    <div class="modal-card" @click="selectFile(file)"  :class="{ 'selected': selectedFileId === file.id }">
      <img src="template/assets/imgs/template/icons/bg-file.png" alt="file">
    </div>
    <p>{{ file.nomfichier.length >= 13 ? file.nomfichier.slice(0, 13) + '...' : file.nomfichier }}</p>
   
   </div>
  </div>

  <div class="modal-footer">
    <button @click="sendFile()" class="send-button">Send</button>
    </div>
</div>

</div>
    </div>
    </body>
  </template>
  <script>
  import axios from "axios";
  import { formatDistance, parseISO,differenceInHours,differenceInSeconds,format } from 'date-fns';
import navbarEntreprise from "@/components/navbarEntreprise.vue";
import navbarEtudiant from "@/components/navbarEtudiant.vue";
import navbarAdmin from "@/components/navbarAdmin.vue";
  export default {
    components: { navbarEntreprise, navbarEtudiant, navbarAdmin },
    data() {
      return {
        messages: [],
        chats:[],
        entreprises:[],
        etudiants:[],
        admin:[],
        newMessage: '',
        baseUrl: "http://localhost:8000",
        userType: "",
        activeUser: null,
        showModal: false,
        newUsername: '',
        activeUsename: "",
      filteredUsernames: [],
      allUsernames: [],// Sample data
      users:[],
      currentUserId: localStorage.getItem("user_id"),
      isModalOpen: false,
      files:[],
      selectedFileId: null,
      selectedFile: null,
      };
    },
    mounted(){
      this.fetchMessages();
      this.fetchFiles();
    },
    created() {
    const userId = localStorage.getItem("user_id");
    
    if (!userId) {
      // User ID not found in local storage, redirect to error interface
      alert("you have to log in");
      this.$router.push("/ConnexionView");
      return;
    }
    // Fetch entreprise data using the entreprise ID
    const userType = localStorage.getItem("user_type");
    // Set userType only if it's valid
    this.userType = userType;
    this.fetchAdminData();
    this.fetchAllEtudiants();
    this.fetchAllEntreprises();
    const username = this.$route.params.username;
  if (username) {
    this.selectUsername(username);
  }
  this.fetchMessages();
  },
    computed: {
      filteredMessages() {
        if (!this.activeUser) return [];
        return this.messages.filter(message => message.username === this.activeUser.username);
      },
     
    },
    methods: {
      openFile(filePath) {
        const fileUrl = `http://127.0.0.1:8000/${filePath}`;
        window.open(fileUrl, '_blank');
    },
sendFile() {
        const userId = this.currentUserId;
        if (this.selectedFile) {
            console.log(this.selectedFile);
            const fileUrl = `http://127.0.0.1:8000/${this.selectedFile}`;
            console.log(fileUrl);

            axios.get(fileUrl, { responseType: 'blob' })
                .then(response => {
                    const fileName = this.selectedFile.split('/').pop(); // Extract the file name from the path
                    const file = new File([response.data], fileName, { type: response.data.type });
                    const formData = new FormData();
                    formData.append('file', file);
           
                    console.log(file);

                    axios.post(`http://127.0.0.1:8000/api/message/${userId}/send/${this.activeUser.id}/`, formData)
                        .then(response => {
                            console.log('message sent', response);
                            this.fetchMessagesBetweenUsers();
                            this.fetchMessages();
                            console.log('Sent:', response.data);
                            this.newMessage = '';
                            this.selectedFileId = null;
                            this.selectedFile = null;
                          this.closeModal();
                        })
                        .catch(error => {
                            console.error('Error sending messages:', error);
                        });
                })
                .catch(error => {
                    console.error('Error fetching the file blob:', error);
                });
        }
    },
    // Other meth
      selectFile(file) {
      this.selectedFileId = file.id;
      this.selectedFile = file.fichier; // Set the selected file
      console.log(`Selected file : ${file.fichier}`);
      console.log(`Selected file with ID: ${file.id}`);
    },
      openModal() {
      this.isModalOpen = true;
      console.log('clicked');
      console.log(this.isModalOpen);

    },
    closeModal() {
      this.isModalOpen = false;
    },
      fetchFiles(){
        axios.get(
          `http://127.0.0.1:8000/get-all-fichiers/${this.currentUserId}`
        )
        .then(response => {
        this.files = response.data;
    console.log(this.files);
        })
        .catch (error => {
        console.error("Error fetching files:", error);
      });
      },
      messageClasses(chat) {
    // Convert sender_id, receiver_id, currentUserId, and activeUser.id to integers
    const senderId = parseInt(chat.sender_id);
    const receiverId = parseInt(chat.receiver_id);
    const currentUserId = parseInt(this.currentUserId);
    const activeUserId = parseInt(this.activeUser.id);

    // Check if the conditions match
    const sentCondition = senderId === currentUserId && receiverId === activeUserId;
    const receivedCondition = senderId === activeUserId && receiverId === currentUserId;

    const classes = [
        'message',
        {
            'sent': sentCondition,
            'received': receivedCondition
        }
    ];
    return classes;
},
      combineUsers() {
        if(this.userType==='admin'){
      this.allUsernames = [
        ...this.etudiants.map(etudiant => etudiant.username),
        ...this.entreprises.map(entreprise => entreprise.username),
        ...this.admin.map(admin => admin.username)
      ];}
      else if(this.userType==='entreprise'){
      this.allUsernames = [
        ...this.etudiants.map(etudiant => etudiant.username),
        ...this.admin.map(admin => admin.username)
      ];
      }
      else if(this.userType==='etudiant'){
      this.allUsernames = [
      ...this.entreprises.map(entreprise => entreprise.username),
        ...this.admin.map(admin => admin.username)
      ];
      }
    },
 Seen() {
  try {
    axios.put(`http://localhost:8000/api/message/seen_message/${this.currentUserId}/`)
      .then(response => {
          console.log('seen',this.messages);
          this.fetchMessages();
          console.log("seen",response);
          console.log("seen");
      })
      .catch(error => {
        console.error('There was an error', error);
      });
  } catch (error) {
    console.error('There was an error :', error);
  }
},
fetchAdminData() {
        axios.get(
          `http://127.0.0.1:8000/api/admin/`
        )
        .then(response => {
        this.admin = response.data;
        this.combineUsers();
        })
    
        .catch (error => {
        console.error("Error fetching admin data:", error);
      });
    },
    fetchAllEtudiants() {
    axios.get('http://127.0.0.1:8000/api/etudiants/getall/')
        .then(response => {
            // Set offers data
            this.etudiants = response.data;
            this.combineUsers();
        })
        .catch(error => {
            // Log error to console
            console.error('Error fetching etudiants:', error);
            // Display alert to the user
            alert('An error occurred while fetching etudiants. Please try again later.');
        });
},
      
      fetchAllEntreprises() {
    axios.get('http://127.0.0.1:8000/api/entreprises/getall/')
        .then(response => {
            // Set offers data
            this.entreprises = response.data;
            this.combineUsers();
        })
        .catch(error => {
            // Log error to console
            console.error('Error fetching entreprises:', error);
            // Display alert to the user
            alert('An error occurred while fetching entreprises. Please try again later.');
        });
},
      formatTimestamp(time) {
      if (!time) return '';
      const date = parseISO(time); // Parse the ISO date string
      return this.customFormatDistanceToNow(date);
    },
   customFormatDistanceToNow(date) {
  const now = new Date();
  const distance = differenceInHours(now, date);
  const distanceInSeconds = differenceInSeconds(now, date);


  if (distanceInSeconds < 60) {
    // If the distance is less than one minute, return the time in "hh.mm" format
    const formattedTime = format(date, 'HH:mm');
    return formattedTime;

  }else if (distance < 24) {
    // If the distance is less than one hour, return the minutes
    const formattedTime = format(date, 'HH:mm');
    return formattedTime;
  } else {
    // If the distance is greater than or equal to one hour, return the hours
    const hours = formatDistance(date, now, { addSuffix: true });
    return hours.replace(' hour', 'h').replace(' hours', 'h').replace(/^about /, '');
  }

},
      getTruncatedTimestamp(time) {
      return time ? time.substring(11,16) : '';
    },
      fetchMessages() {
        const userId = localStorage.getItem("user_id");
      axios.get(`http://127.0.0.1:8000/api/message/get_recipient_or_sender/${userId}/`)
        .then(response => {
          // Assign the fetched offers to the offers array
          this.messages = response.data;
          console.log("messages",this.messages);

        
        })
        .catch(error => {
          console.error('Error fetching messages:', error);
        });
      },
      sendMessage() {
        const userId = localStorage.getItem("user_id");
        if (this.newMessage.trim() !== '') {
           const data={
            body:this.newMessage,
            
           }
        axios.post(`http://127.0.0.1:8000/api/message/${userId}/send/${this.activeUser.id}/`,data)
        .then(response => {
          console.log('message sent', response);
          const newMessage = {
                    body: this.newMessage,
                    sender_id: userId,
                    recipient_id: this.activeUser.id,
                    timestamp: new Date().toISOString(),
                };
                this.fetchMessagesBetweenUsers();
                this.fetchMessages();
                console.log('Sent:', newMessage); // Log whether the message is sent
     
           
                this.newMessage = '';
        
          })
        .catch(error => {
          console.error('Errorsending messages:', error);
        });
      }
      },
      openNewMessageModal() {
        this.showModal = true;
      },
      closeNewMessageModal() {
        this.showModal = false;
        this.newUsername = '';
        this.filteredUsernames = [];
      },
      filterUsernames() {
      const query = this.newUsername.toLowerCase();
      this.filteredUsernames = this.allUsernames.filter(username => username.toLowerCase().startsWith(query));
    },
    fetchUsername(username){
      axios.get(`http://127.0.0.1:8000/api/get_user_username/${username}/`)
          .then(response => {
            this.activeUser = response.data;
            console.log('username:',this.activeUser);
            this.handleActiveUserActions();
          })
          .catch(error => {
            console.error('Error fetching username:', error);
          });


    },
    selectUsername(username) {
      this.activeUser = this.users.find(user => user.username === username) || { username, timestamp: new Date().toLocaleTimeString() };

        if (!this.users.find(user => user.username === username)) {
            this.fetchUsername(username);
        } else {
            // If user is already found in users array, directly handle actions
            this.handleActiveUserActions();
        }
    },
    handleActiveUserActions() {
        if (this.activeUser && this.activeUser.id) {
            console.log('here', this.activeUser.id);
            if (!this.users.find(user => user.id === this.activeUser.id)) {
                this.users.push(this.activeUser);
            }
            this.closeNewMessageModal();
            this.openChat(this.activeUser.id);
            this.fetchMessagesBetweenUsers();
        }
    },
    openChat(user) {
      axios.get(`http://127.0.0.1:8000/api/get_user/${user}/`)
          .then(response => {
            this.activeUser = response.data;
            this.users.push(this.activeUser);
            this.Seen();
            this.fetchMessages();
            this.fetchMessagesBetweenUsers(user);
          console.log('user:',this.activeUser);
            console.log('user_id:',user);
          })
          .catch(error => {
            console.error('Error fetching user data:', error);
          });

    },
    fetchMessagesBetweenUsers() {
      const userId = localStorage.getItem("user_id");
      axios.get(`http://127.0.0.1:8000/api/message/get_messages_between_users/${userId}/${this.activeUser.id}/`)
        .then(response => {
          this.chats = response.data;
          console.log(this.chats);
      })
        .catch(error => {
          console.error('Error fetching messages between users:', error);
        });
    }
    }
  };
  </script>
  
  <style scoped>
  .modal-body-2{
    display: flex;
    flex-wrap: wrap;
    align-content: center;
    justify-content: center;
    align-items: center;

  }
  .container-file{
    display:flex;
    align-items:center;
  }
  .container-file p{
 font-size:20px;
  }
  .modal-footer {
  padding: 2px 16px;
  background-color: #fff;

}
  .modal-card.selected {
  border: 2px solid #447AB8;
}
 .container-cards-modal p{
   display: flex;
    justify-content: center;
    margin-bottom:10px;
  }
  .container-cards-modal{
    border: 1px solid transparent;
    margin:20px;
    margin-right:40px !important;
margin-left:40px !important;
margin-bottom: 30px;
width:130px;
height:130px;
  }
  .modal-header-2 {
  padding: 2px 16px;
  background-color: #fff;
  height:60px;
  margin-top:20px;
  margin-bottom:20px;
  margin-left:20px;
  padding-bottom:10px;
  border-bottom:1px solid#dee2e6;
}
  .modal-card{
    display: flex;
    justify-content: center;
    align-items: center;
    background-color:#fff;
    border:#dee2e6 1px solid;
border-radius:10px;
    height:100px;
    width:100px;
    padding:10px;
    margin:20px;
    margin-bottom:5px;
  }
  .modal-2 {
  
  display: block; /* Hidden by default */
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  padding-bottom: 100px;
  padding-top: 100px; /* Location of the box */
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: rgb(0, 0, 0); /* Fallback color */
  background-color: rgba(0, 0, 0, 0.4); /* Black w/ opacity */
}

  /* Modal Content */

.modal-content-2 {
  border-radius:20px;

  position: relative;
  background-color: #fefefe;
  margin: auto;
  padding: 0;
  border: 1px solid #888;
  width: 80%;
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2),0 6px 20px 0 rgba(0,0,0,0.19);
  -webkit-animation-name: animatetop;
  -webkit-animation-duration: 0.4s;
  animation-name: animatetop;
  animation-duration: 0.4s
}

/* Add Animation */
@-webkit-keyframes animatetop {
  from {top:-300px; opacity:0} 
  to {top:0; opacity:1}
}

@keyframes animatetop {
  from {top:-300px; opacity:0}
  to {top:0; opacity:1}
}

/* The Close Button */
.close-2 {
  color: #000;
  float: right;
  font-size: 28px;
  font-weight: bold;
  top: -60px;
    position: relative;
}

.close-2:hover,
.close-2:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
}



.modal-body {padding: 2px 16px;}

.modal-footer-2 {
  padding: 2px 16px;
  background-color: #5cb85c;
  color: white;
}
  .bold-weight{
    font-weight: 1000;
  }
  .home-page-chat p{
    display: flex;
    justify-content: center;
  }
  .cards-chat{
    height: 150px;
    background-color: #fff;
    width: 200px;
    margin: 10px;
  }
  .home-page-chat{
    height:100%;
  }
  .card-container img{
width: 350px;
  }
  .card-container{
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    height: 500px;
    position: relative;
    top: 100px;

    padding: 30px;
  }
    .chat-header {
    background-color: #fff;
    color: white;
    padding: 20px;
    border-bottom:1px solid#dee2e6;
    height:60px;
  }
  .chat-header h6{
    color:#447AB8 ;
    position: relative;
    left: 60px;
    bottom: 70px;
  }
  .chat-header img{
    padding:10px;
    position: relative;
    width: 60px;
    height: 60px; /* Set height equal to width */
    border-radius: 50%;
    bottom:20px;

  }
.message.just-sent {
  align-self: flex-end;
    text-align: right;
}
.message.sent {
    align-self: flex-end;
    text-align: right;
}
.message.sent .message-content{
  background-color: #447AB8;
  color:#fff;
}


.message.received {
  align-self: flex-start;
  text-align: left;
}

.message-content {
  margin-bottom: 5px;
}


  .modal-title{
    font-size: 28px;
    margin-bottom:10px;
  }
  .chat-app {
    display: flex;
    height: 100vh;
    width: 100%;
    margin: 0 auto;
    overflow: hidden;
  }
  
  .sidebar {
    width: 350px;
    background-color: #f2f4fa;
    color: #447AB8;
    padding: 20px;
    display: flex;
    flex-direction: column;

  }
  .new-message-btn img{
    width:40px;
  }
  .new-message-btn {
    background-color: #f2f4fa;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    margin-bottom: 20px;
    font-size: 16px;
    width: 50px;
    height: 50px;
    margin-left:270px;
    display:flex;
    align-items:center;
    justify-content:center;
  }
  
  .new-message-btn:hover {
    background-color: #e4ebff;
  }


  .users-list h2 {
    font-size: 18px;
    margin-bottom: 10px;
  }
  
  .users-list ul {
    list-style-type: none;
    padding: 0;
    font-family: "Plus Jakarta Sans", sans-serif;
    font-style: normal;
    font-weight: bold;
    font-size: 18px;
    line-height: 24px;
      }
  .text-message{
    color:#858585;
    font-size: 14px;
    font-weight: normal;
  }
.container-message{
    width: 200px;
    height: 50px;
    margin-left: 20px;
    flex-direction: column;
    margin-bottom: 10px;
    display:flex;
  }
  .users-list li {
    padding: 10px;
    border-bottom: 1px solid #dee2e6;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
    height:100px;
  }
  .username {
    font-weight: bold;
    margin-bottom: 5px; 
   /* margin-right: 200px;*/
  }
  .profile img{
    width:50px !important;
    height: 50px; /* Set height equal to width */
    border-radius: 50%;
    max-width: none !important;

  }
  .profile {
    width:50px !important;
    max-width: 100%;
  }
    
    
  .timestamp {
    font-size: 12px;
    color: #858585;
    margin-top:-50px;
    width:60px;
  }
  
  .chat-container {
    flex: 1;
    display: flex;
    flex-direction: column;
  }
  

  .chat-window {
    flex: 1;
    overflow-y: auto;
    padding: 20px;
    background-color: #fff;
  }
  
  .messages {
    display: flex;
    flex-direction: column;
  }
  
  .message {
    margin-bottom: 10px;
    max-width: 70%;
  }
  

  
  .message-content {
    padding: 10px 15px;
    border-radius: 15px;
    background-color: #ecf0f1;
  }
  
  .chat-footer {
    display: flex;
    padding: 10px;
    background-color: white;
    border-top: 1px solid #ddd;
  }
  
  .chat-input {
    flex: 1;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 20px;
    outline: none;
  }
  
  .send-button {
    background-color: #447AB8;
    color: white;
    border: none;
    padding: 10px 20px;
    margin-left: 10px;
    border-radius: 20px;
    cursor: pointer;
  }
  
  .send-button:hover {
    background-color: #2980b9;
  }
  
  .modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .modal-content {
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    width: 400px;
    position: relative;
  }
  
  .close {
    position: absolute;
    top: 10px;
    right: -150px;
    font-size: 20px;
    cursor: pointer;
  }
  
  .username-input {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border-radius: 5px;
    border: 1px solid #ddd;
  }
  
  .suggestions {
    list-style-type: none;
    padding: 0;
    margin: 0;
    border: 1px solid #ddd;
    border-radius: 5px;
    background-color: white;
  }
  
  .suggestions li {
    padding: 10px;
    cursor: pointer;

  }
  .name{
    position: relative;
    left: -130px;
  }
  
  .suggestions li:hover {
    background-color: #ecf0f1;
  }
  </style>
  
  