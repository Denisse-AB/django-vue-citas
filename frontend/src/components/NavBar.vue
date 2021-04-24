<template>
  <div>
      <b-navbar id="fixed" variant="light" class="shadow fixed-top " type="light">
        <b-navbar-nav>
          <b-nav-item href="/">{{ 'Inicio' }}</b-nav-item>
        <!-- logo -->
        </b-navbar-nav>
            <b-navbar-brand class="mx-auto" href="/">
              <img alt="Vue logo" src="../assets/logo.png">
            </b-navbar-brand>
        <!-- dropdown -->
        <b-navbar-nav>
        </b-navbar-nav>
      </b-navbar>
    <AppForm msg="Bienvenidos" />
  </div>
</template>

<script>
import AppForm from './AppForm'

export default {
  name: 'App',
  components: {
    AppForm
  }
}
</script>

<style lang="scss">
img {
  height: 60px;
}
</style>
