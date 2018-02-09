<template>
<div id="app">
    <nav id="nav-top" class="uk-navbar-container uk-box-shadow uk-background-secondary" uk-navbar>
        <div class="uk-navbar-left">
            <a class="uk-navbar-item uk-logo" href="#">Thousandblurbs</a>
        </div>
        <div class="uk-navbar-left">
          <ul class="uk-navbar-nav">
                <li>
                    <router-link to="/admin/">
                        My Blurbs <span class="uk-margin-small-left" uk-icon="icon: folder"></span>
                    </router-link>
                </li>
            </ul>
        </div>
        <div class="uk-navbar-right">
            <ul class="uk-navbar-nav">
                <!--
                <li>
                    <router-link to="/signout/">
                        Settings <span class="uk-margin-small-left" uk-icon="icon: cog"></span>
                    </router-link> 
                </li>
                -->
                <li>
                    <a href="/signout/">Sign Out <span class="uk-margin-small-left" uk-icon="icon: sign-out"></span></a> 
                </li>
            </ul>
        </div>
    </nav>
    <div>
      <router-view></router-view>
    </div>
</div>
</template>

<script>
export default {
    name: "app",
    data() {
        return {
            
        }
    },
    methods: {
        goBack() {
            window.history.length > 1
            ? this.$router.go(-1)
            : this.$router.push('/');
        },
        iconClass(icon) {
            return `icon: ${icon}`;
        }
    }
};
</script>