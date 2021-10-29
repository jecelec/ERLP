<template>
    <div class="home">
        <h1>Bienvenido {{ username }} </h1><br>
        <h2>Datos reportados en ARL Positiva en Colombia 2021:</h2> 
        <h3>132 muertes por accidente laboral</h3>  
        <h3>555 incapacidades</h3>      
        <h3>25 pensiones por accidente de trabajo</h3>             
        <h3>35 pensiones por enfermedad laboral</h3>             
        <h3>25 incapacidades por accidente de trabajo</h3>             
        <h3>51 incapacidades por enfermedad laboral</h3>                  
    </div>
</template>


<script>
    export default{
        name: "Home",

        data: function(){
            return {
                username: localStorage.getItem("username") || "none"
            }
        }
    }
</script>


<style>
    .home {
        margin         : 0;
        padding        : 0%;
        height         : 100%;
        width          : 80%;
        justify-content: center;
        align-items    : center;
    }

    .home h1 {
        font-size: 50px;
        color    : #24304c;
    }
</style>