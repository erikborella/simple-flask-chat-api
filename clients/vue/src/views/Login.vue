<template>
    <v-app>
        <v-container fluid class="fill-height">
             <v-row align="center" justify="center">
                <v-col cols="12" sm="8" md="5">

                    <v-card class="elevation-12">

                            <v-toolbar color="primary" dark flat>
                                <v-toolbar-title>Login</v-toolbar-title>
                                <v-spacer/>
                                <v-btn elevation="0" color="primary">
                                    Cadastrar
                                </v-btn>
                            </v-toolbar>

                            <v-card-text>
                                <v-form>

                                    <v-text-field
                                        name="email"
                                        label="Email"
                                        id="email"
                                        :rules="rules.emailRules"
                                        v-model="email"/>
                                    <v-text-field
                                        name="password"
                                        label="Senha"
                                        id="password"
                                        type="password"
                                        :rules="rules.passwordRules"
                                        v-model="password"/>
                                        
                                </v-form>
                            </v-card-text>

                            <v-card-actions>
                                <v-btn class="px-4" color="primary">Logar</v-btn>
                            </v-card-actions>
                    </v-card>

                </v-col>
            </v-row>
        </v-container>
    </v-app>
</template>

<script>
export default {
    data: () => ({
        email: "",
        password: "",
        rules: {
            emailRules: [
                v => !!v || "Email é obrigatorio"
            ],
            passwordRules: [
                 v => !!v || "Senha é obrigatoria"
            ]
        }
    })
}
</script>
