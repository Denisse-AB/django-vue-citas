<template>
  <div class="mx-auto w-75 mt-5 padding">
    <div id="card" class="position-relative p-4">
      <p class="text-dark font-weight-bold">
        {{ msg }}!
      </p>
      <b-card class="shadow-sm">
        <!-- form -->
        <b-form @submit.prevent="Submit">
        <b-container v-show="card" fluid>

          <b-row class="my-1">
            <b-col sm="2">
              <label for="input-default">E-mail:</label>
            </b-col>

            <b-col sm="10">
              <ValidationProvider name="email" rules="required|email" v-slot="{ errors }">
              <b-form-input
                v-model="email"
                type="email"
                :class="{'is-invalid' : errors[0]}" :placeholder="'email'"
                trim
              ></b-form-input>
               <div class="error mt-1">{{ errors[0] }}</div>
              </ValidationProvider>
            </b-col>
          </b-row>

          <b-row class="my-3">
            <b-col sm="2">
              <label for="input-default">{{ 'Nombre' }}:</label>
            </b-col>
            <b-col sm="10">
              <ValidationProvider name="name" rules="required|alpha_spaces" v-slot="{ errors }">
               <b-form-input
                 v-model="name"
                 :class="{'is-invalid' : errors[0]}" placeholder="Tu nombre, solo letras permitidas"
                 trim
                ></b-form-input>
               <div class="error mt-1">{{ errors[0] }}</div>
              </ValidationProvider>
            </b-col>
          </b-row>

          <b-row class="my-3">
            <b-col sm="2">
              <label for="input-default">Tel:</label>
            </b-col>
            <b-col sm="10">
          <ValidationProvider name="phone" rules="required|digits:10" v-slot="{ errors }">
            <b-form-input
              v-model="tel"
              :class="{'form-control': 'true', 'is-invalid' : errors[0]}" placeholder="Telefono, ingresar 10 numeros solamente"
              trim
            ></b-form-input>
            <div class="error mt-1">{{ errors[0] }}</div>
          </ValidationProvider>
            </b-col>
          </b-row>

          <!-- div for pickers -->
          <b-row>
            <b-col class="mt-3" md>
              <b-form-datepicker
                v-model="date"
                :date-disabled-fn="dateDisabled"
                placeholder="Escoge un dia"
                locale="es"
              ></b-form-datepicker>
            </b-col>
            <b-col class="mt-3" md>
              <b-form-select
                v-model="time"
                :options="options"
              ></b-form-select>
            </b-col>
          </b-row>

        </b-container>
          <b-button
            v-show="card"
            class="mt-3"
            :disabled="spinner"
            variant="success"
            type="submit"
          >
            {{ 'Ingresar' }}
          </b-button>
        </b-form>
        <!-- thankyou note -->
        <div v-show="icon">
          <p id="icon"><b-icon-check-circle-fill></b-icon-check-circle-fill> {{ 'Gracias' }}!</p>
          <h5 class="offset-3 msg">{{ 'Verifica tu email' }} !</h5>
          <hr>
          <p class="mt-4">{{ 'Su cita fue aceptada para:' }} <strong>{{ data.date }}</strong> {{ 'a las' }} <strong>{{ data.time }}</strong></p>
        </div>
      </b-card>
      <p v-show="response" class="text-danger font-weight-bold mb-0 mt-2">
        {{ 'Turno agotado, favor escoger otra hora o dia.' }}
      </p>
      <b-overlay
        :show="spinner"
        no-wrap
      ></b-overlay>
    </div>
    <br>
    <br>
    <footer class="mt-2">Copyright &copy; 2021 Denisse AB Image: Vue.js</footer>
  </div>
</template>

<script>
import { BFormInput, BFormDatepicker, BForm, BButton, BIconCheckCircleFill } from 'bootstrap-vue'
import { ValidationProvider } from 'vee-validate'
import PostService from '../post-service'
import '../validation'

export default {
  name: 'AppForm',

  props: {
    msg: String
  },

  components: {
    ValidationProvider,
    BFormInput,
    BForm,
    BFormDatepicker,
    BIconCheckCircleFill,
    BButton
  },

  data () {
    return {
      spinner: false,
      card: true,
      icon: false,
      response: false,
      data: {},
      email: '',
      name: '',
      date: '',
      tel: '',
      csrftoken: '',
      time: null,
      options: [
        { value: null, text: 'Escoja una Hora' },
        { value: '12:00:00', text: '12:00 PM' },
        { value: '13:00:00', text: '1:00 PM' },
        { value: '14:00:00', text: '2:00 PM' },
        { value: '15:00:00', text: '3:00 PM' }
      ]
    }
  },

  async mounted () {
    if (document.cookie && document.cookie !== '') {
      // TODO: split token ;
      const token = document.cookie.split('=')
      if (token[0] === 'csrftoken') {
        this.csrftoken = decodeURIComponent(token[1]).trim()
      }
    }
  },

  methods: {
    dateDisabled (ymd, date) {
      // Disable weekends (Sunday = `0`, Saturday = `6`) and
      // disable days that fall on the 5th of the month
      const weekday = date.getDay()
      const day = date.getDate()
      // Return `true` if the date should be disabled
      return weekday === 0 || weekday === 6 || day === 5
    },

    async Submit () {
      this.spinner = true
      this.data = {}

      try {
        await PostService.insertPost(
          this.email, this.name, this.date, this.tel, this.time, this.csrftoken

        ).then(res => {
          if (res.status === 201) {
            this.email = ''
            this.name = ''
            this.date = ''
            this.tel = ''
            this.time = ''
            this.card = false
            this.spinner = false
            this.icon = true
            this.response = false
            this.data = res.data
          }

          if (res.status === 200) {
            this.spinner = false
            this.response = true
          }
        })
      } catch (err) {
        alert('Ha ocurrido un error!')
        this.spinner = false
      }
    }
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
$green-bg: #c6ebd9;
$error: red;
$green: green;
$sm : 576px;

#card {
  background-color: $green-bg;
}

.form-control.focus, .form-control:focus, .custom-select:focus {
  border-color: $green;
  box-shadow: 0 0 0 0.2rem rgba(77, 192, 181, 0.25);
}

.padding {
  padding-top: 100px;
}

.error {
  color: $error;
}

#icon {
  font-size: 70px;
  color: $green;
}

.msg{
  font-family: 'Raleway', sans-serif;
}

@media (max-width: $sm) {
  #icon {
    font-size: 40px;
  }
}
</style>
