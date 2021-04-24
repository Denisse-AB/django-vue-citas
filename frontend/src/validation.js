/* eslint-disable camelcase */
import { extend } from 'vee-validate'
import { required, email, alpha_spaces, digits } from 'vee-validate/dist/rules'

// Install required rule and message.
extend('required', {
  ...required,
  message: 'Este campo es requerido'
})

extend('email', {
  ...email,
  message: 'El campo {_field_} es invalido'
})

extend('alpha_spaces', {
  ...alpha_spaces,
  message: 'Solo letras permitidas'
})

extend('digits', {
  ...digits,
  message: 'Solo numeros permitidos'
})
