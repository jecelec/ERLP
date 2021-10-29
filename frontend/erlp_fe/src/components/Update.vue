<template>
    <div class="">
        <div class="form-register">
            <h2>Reporte de riesgo ARL Positiva</h2>
            <form v-on:submit.prevent="processSignUp" >
                <input class = "controls" type = "number"   name = "ID" id ="id" placeholder = "ID del reporte">
                <input class = "controls" type = "text"   name = "Departamento" id ="departamento" placeholder = "Departamento">
                <input class = "controls" type = "text"   name = "Municipio" id ="municipio" placeholder = "Municipio">
                <input class = "controls" type = "number" name = "Codigoarl" id ="codigo_arl" placeholder = "Codigo ARL">
                <input class = "controls" type = "number" name = "Year" id ="year" placeholder = "Año">
                <input class = "controls" type = "number" name = "Month" id ="month" placeholder = "Mes">
                <input class = "controls" type = "number" name = "Sector economico" id ="economia" placeholder = "Actividad económica">
                <input class = "controls" type = "number" name = "Relacion dependiente" id ="rela_dep" placeholder = "Relacion dependiente">
                <input class = "controls" type = "number" name = "Relacion independiente" id ="rela_indep" placeholder = "Relación independiente">
                <input class = "controls" type = "number" name = "Presunción de accidente" id ="presu_acci_rasu" placeholder = "Presunción de accidente">
                <input class = "controls" type = "number" name = "Muertes Accidente de trabajo" id ="muertes_AT" placeholder = "Muertes accidente de trabajo">
                <input class = "controls" type = "number" name = "Muertes Enfermedad Laboral" id ="muerte_EL" placeholder = "Muertes enfermedad laboral">
                <input class = "controls" type = "number" name = "Incapacidades Enfermedad Laboral" id ="incapacidad_EL" placeholder = "Incapacidades enfermedad laboral">
                <input class = "controls" type = "number" name = "Incapacidades Accidente de trabajo" id ="incapacidad_AT" placeholder = "Incapacidades de accidente de trabajo">
                <p>El manejo de la información está basado en la Ley 1581 de Habeas Data</p>
                <input class = "botons" type= "submit" value = "Modificar">


                <!-- <button type="submit">Registrarse</button> -->
            </form>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        name: "Update",

        data: function(){
            return {
                user: {
                    username: "",
                    password: "",
                    name: "",
                    email: "",
                    account: {
                        lastChangeDate: (new Date()).toJSON().toString(),
                        balance       : 0,
                        isActive      : true
                    }
                }
            }
        },

        methods: {
            processSignUp: function(){
                console.log(this.user);
                axios.post(
                    "http://localhost:8000/user/",
                    this.user,
                    {headers: {}}
                )
                .then((result) => {
                    let dataSignUp = {
                        username      : this.user.username,
                        tokenAccess  : result.data.access,
                        tokenRefresh : result.data.refresh,
                    }
                    this.$emit('completedSignUp', dataSignUp)
                })
                .catch((error) => {
                    console.log(error)
                    alert("ERROR: Fallo en el registro.");
                });
            }
        }
    }
</script>

<style>
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}


.form-register{
    width: 400px;
    background: #24304c;
    padding: 30px;
    margin: auto;
    margin-top: 100pz;
    border-radius: 4px;
    font-family: 'calibri';
    color: white;


}


body{
    background-color:rgb(255, 255, 255);

}

.form-register h4{
    font-size: 33px;
    margin-bottom: 20px;

}

.controls{
    width: 100%;
    background: #24303c;
    padding:10px;
    border-radius: 4px;
    margin-bottom: 16px;
    border: 1px solid #1f53c5;
    color: white;
}

.form-register p {
    height: 40px;
    text-align: center;
    font-size: 18px;
}

.form-register a {
    color: white;
    text-decoration: none;
}

.form-register a:hover {
    color: white;
    text-decoration: underline;

}

.form-register .botons{
    width:100%;
    background: #1f53c5;
    border: none;
    padding: 12px;
    color: white;
    margin: 16px 0;
    font-size: 16px;


}

</style>