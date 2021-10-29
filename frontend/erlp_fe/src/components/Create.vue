<template>
    <div class="">
        <div class="form-register">
            <h2>Reporte de riesgo ARL Positiva</h2>
            <form v-on:submit.prevent="processCreate" >                
                <input class = "controls" type = "text"   name = "departamento"         id ="departamento"       placeholder = "Departamento">                          
                <input class = "controls" type = "text"   name = "municipio"            id ="municipio"          placeholder = "Municipio">
                <input class = "controls" type = "number" name = "codigo_arl"           id ="codigo_arl"         placeholder = "Codigo ARL">
                <input class = "controls" type = "number" name = "year"                 id ="year"               placeholder = "Año">
                <input class = "controls" type = "number" name = "month"                id ="month"              placeholder = "Mes">
                <input class = "controls" type = "number" name = "economia"             id ="economia"           placeholder = "Actividad económica">
                <input class = "controls" type = "number" name = "rela_dep"             id ="rela_dep"           placeholder = "Relacion dependiente">
                <input class = "controls" type = "number" name = "rela_indep"           id ="rela_indep"         placeholder = "Relación independiente">
                <input class = "controls" type = "number" name = "presu_acci_rasu"      id ="presu_acci_rasu"    placeholder = "Presunción de accidente">
                <input class = "controls" type = "number" name = "muertes_AT"           id ="muertes_AT"         placeholder = "Muertes accidente de trabajo">
                <input class = "controls" type = "number" name = "pensiones_AT"         id ="pensiones_AT"       placeholder = "pension por accidente de trabajo">
                <input class = "controls" type = "number" name = "pensiones_EL"         id ="pensiones_EL"       placeholder = "pension por accidente de trabajo">
                <input class = "controls" type = "number" name = "incapacidades_EL"     id ="incapacidad_EL"     placeholder = "Incapacidades enfermedad laboral">
                <input class = "controls" type = "number" name = "incapacidades_AT"     id ="incapacidad_AT"     placeholder = "Incapacidades de accidente de trabajo">
                <p>El manejo de la información está basado en la Ley 1581 de Habeas Data</p>
                <input class = "botons" type= "submit" value = "Crear">


                <!-- <button type="submit">Registrarse</button> -->
            </form>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        name: "Create",

        data: function(){
            return {
                user: {
                    departamento:       "",
                    municipio:          "",
                    codigo_arl:         "",
                    year:               "",
                    month:              "",
                    economia:           "",
                    rela_dep:           "",
                    rela_indep:         "",
                    presu_acci_rasu:    "",
                    muertes_AT:         "",
                    pensiones_AT:       "",
                    pensiones_EL:       "",
                    incapacidades_EL:   "",
                    incapacidades_AT:   "",                    
                }
            }
        },

        methods: {
            processCreate: function(){
                console.log(this.user);
                axios.post(
                    "http://localhost:8000/statistics/crear/",
                    this.user,
                    {headers: {}}
                )
                .then((result) => {
                    let dataCreate = {
                        departamento    : this.historico.departamento,
                        municipio       : this.historico.municipio,
                        codigo_arl      : this.historico.codigo_arl,
                        year            : this.historico.year,
                        month           : this.historico.month,
                        economia        : this.historico.economia,
                        rela_dep        : this.historico.rela_dep,
                        rela_indep      : this.historico.rela_indep,
                        presu_acci_rasu : this.historico.presu_acci_rasu,
                        muertes_AT      : this.historico.muertes_AT,
                        muerte_EL       : this.historico.muerte_EL,
                        incapacidad_EL  : this.historico.incapacidad_EL,
                        incapacidad_AT  : this.historico.incapacidad_AT
                    }
                    this.$emit('completedCreate', dataCreate)
                })
                .catch((error) => {
                    console.log(error)
                    alert("Error al crear registro.");
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