import Vue from 'vue'
import VueI18n from 'vue-i18n'
import es from 'vee-validate/dist/locale/es.json'
import en from 'vee-validate/dist/locale/en.json'

Vue.use(VueI18n)

const i18n = new VueI18n({
  locale: 'es',
  fallbackLocale: 'en',
  messages: {
    es: {
      Home: 'Inicio',
      Lang: 'Idioma',
      Welcome: 'Bienvenido',
      email: 'Ingresa tu correo electrónico',
      name: 'Nombre',
      nameHolder: 'Ingresa tu nombre completo',
      tel: 'Ingresa tu número de teléfono',
      calendar: 'es',
      dateHolder: 'Escoja una fecha',
      hour: 'Escoja un hora',
      Submit: 'Enviar',
      Thankyou: 'Gracias',
      check: 'Verifica tu Email',
      day: 'Tu cita fue aceptada para el día',
      time: 'a las',
      message: 'Turno agotado, escoja otra Hora o Día.',
      alert: 'Favor de tratar de nuevo!',
      fields: {
        email: 'Correo electrónico',
        name: 'nombre',
        phone: 'teléfono'
      },
      validation: es.messages
    },
    en: {
      Home: 'Home',
      Lang: 'Lang',
      Welcome: 'Welcome',
      email: 'Enter Your Email',
      name: 'Name',
      nameHolder: 'Enter your full Name',
      tel: 'Enter your Telephone Number',
      calendar: 'en',
      dateHolder: 'Choose a date',
      hour: 'Choose an hour',
      Submit: 'Submit',
      Thankyou: 'Thankyou',
      check: 'Check Your Email',
      day: 'Your appointment was accepted for',
      time: 'at',
      message: 'Not available, choose a different time or day.',
      alert: 'Something went wrong, try again!',
      fields: {
        email: 'E-mail',
        name: 'name',
        phone: 'phone number'
      },
      validation: en.messages
    }
  }
})

export default i18n
