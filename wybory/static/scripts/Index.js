//import * as moment from 'moment'
var Index = /** @class */ (function () {
    function Index() {
        var _this = this;
        this.init = function () {
            setInterval(_this.calcAllTimes, 1000);
        };
        this.calcAllTimes = function () {
            var elems = $('.sp-calc-time[data-time]');
            elems.each(function (index, Elem) {
                var item = $(Elem);
                var duration = moment.duration(moment(item.attr('data-time')).diff(moment()));
                //const daysLeft = ;
                //const hoursLeft: number = moment(item.attr('data-time')).diff(now, 'hours');
                //const minutesLeft: number = moment(item.attr('data-time')).diff(now, 'minutes');
                //const secondsLeft: number = moment(item.attr('data-time')).diff(now, 'seconds');
                item.text("Zosta\u0142o " + duration.days() + " dni, " + duration.hours() + " godzin " + duration.minutes() + " minut, " + duration.seconds() + " sekund");
            });
        };
    }
    return Index;
}());
var index = new Index();
$(document).ready(function () {
    index.init();
});
