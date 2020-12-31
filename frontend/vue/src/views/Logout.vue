<template>
<p>logout</p>
</template>

<script>
export default{
beforeMount(){
this.$emit("recant");
localStorage.removeItem("isAuthenticated_lifenote");
localStorage.removeItem("token_lifenote");
// this.$forceUpdate();
this.$router.push("/")
}
}
</script>

<style lang="scss" scoped>

</style>