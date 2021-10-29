<template>
  <div id="app" class="app">
    <div class="header">
      <h2>ERLP Estadística de riesgos laborales Positiva</h2>
      <nav>
        <button v-if="isAuth" v-on:click="loadHome"> Inicio </button>
        <button v-if="isAuth" v-on:click="loadCreate"> Crear registro </button>
        <button v-if="isAuth" v-on:click="loadUpdate"> Modificar registro </button>
        <button v-if="isAuth" v-on:click="loadView"> Buscar registro </button>
        <button v-if="isAuth" v-on:click="loadDelete"> Eliminar registro </button>
        <button v-if="isAuth" v-on:click="logOut"> Cerrar Sesión </button>

        <button v-if="!isAuth" v-on:click="loadLogIn"> Iniciar Sesión </button>
        <button v-if="!isAuth" v-on:click="loadSignUp"> Registrarse </button>
      </nav>
    </div>

    <div class="main-component">
      <router-view
        v-on:completedLogIn="completedLogIn"
        v-on:completedSignUp="completedSignUp"
        v-on:logOut="logOut"
      >
      </router-view>
    </div>

    <div class="footer">
      <h2>MisionTic 2022 - P46 Grupo 1</h2>
    </div>
  </div>
</template>


<script>
  export default{
    name: 'App',

    data: function(){
      return {
        isAuth: false
      }
    },

    components:{
    },

    methods:{
      verifyAuth: function(){
        this.isAuth = localStorage.getItem("isAuth") || false;
        if(this.isAuth == false){
          this.$router.push({name: "login"})
        }
        else{
          this.$router.push({name: "home"});
        }
      },
      
      loadHome: function(){
        this.$router.push({name: "home"});
      },
      
      loadCreate: function(){
        this.$router.push({name: "create"});
      },
      
      loadDelete: function(){
        this.$router.push({name: "delete"});
      },
      
      loadUpdate: function(){
        this.$router.push({name: "update"});
      },
      
      loadView: function(){
        this.$router.push({name: "view"});
      },

      loadAccount: function(){
        this.$router.push({name: "account"});
      },

      logOut: function(){
        localStorage.clear();
        alert("Sesión terminada");
        this.verifyAuth();
      },

      loadLogIn: function(){
        this.$router.push({name: "login"})
      },

      loadSignUp: function(){
        this.$router.push({name: "signUp"})
      },

      completedLogIn: function(data){
        localStorage.setItem('username', data.username);
        localStorage.setItem('tokenRefresh', data.tokenRefresh);
        localStorage.setItem('tokenAccess', data.tokenAccess);
        localStorage.setItem('isAuth', true);
        alert("Autenticación exitosa");
        this.verifyAuth();
      },

      completedSignUp: function(data){
        alert("Registro exitoso");
        this.completedLogIn(data);
      },
    },

    created: function(){
      this.verifyAuth();
    }
  }
</script>

<style>
  body {
    max-width: 0 0 0 0;
  }

  .header{
    margin: 0;
    padding: 15px;
    width: 100%;
    height: 10vh;
    min-height: 100px;
    background-color: #24304c ;
    color:#E5E7E9 ;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .header h1{
    width: 20%;
    text-align: center;
  }

  .header nav {
    height: 100%;
    width: 40%;
    display: flex;
    justify-content: space-around;
    align-items: center;
    font-size: 20px;
  }

  .header nav button{
    color: #E5E7E9;
    background: #24304c;
    border: 1px solid #E5E7E9;
    border-radius: 5px;
    padding: 10px 20px;
    margin: 3px;
  }

  .header nav button:hover{
    color: #E5E7E9;
    background: #060874;
    border: 1px solid #E5E7E9;
  }

  .main-component{
    height: 95%;
    margin: 3%;
    padding: 0%;
    background: #FDFEFE ;
    align-content: center;
  }

  .footer{
    margin: 0;
    padding: 0;
    width: 100%;
    height: 10vh;
    min-height: 100px;
    background-color: #24304c;
    color: #E5E7E9;
  }

  .footer h2{
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>
