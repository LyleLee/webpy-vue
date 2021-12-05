$(document).ready(function () {

    var app = new Vue({
        el: '#app',
        data: {
            date: '',
            title: 'initial value',
            url: '',
            info: null
        },

        created: function () {
            var _this = this;
            console.log(">>", location.host);
            console.log(">>", location.protocol)
            $.getJSON('http://' + location.host + '/static/json/news.json', function (json) {
                _this.date = json[0]["2021-11-02"][0].news_creation_time;
                _this.title = json[0]["2021-11-02"][0].title;
                _this.url = json[0]["2021-11-02"][0].news_web_url;
            });
        },

        mounted() {
            axios.get('http://' + location.host + '/api/json/nhk.json').then(response => {
                console.log(typeof response.data);
                this.info = response.data;
                console.log();
            });
        }
    });
});