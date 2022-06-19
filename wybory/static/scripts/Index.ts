//import * as moment from 'moment'

class Index {
    public init = (): void => {
        setInterval(this.calcAllTimes, 1000);
    }

    private calcAllTimes = () : void => {
        let elems = $('.sp-calc-time[data-time]');
        elems.each((index: number, Elem: Element) => {
            const item = $(Elem);
            const duration = moment.duration(moment.utc(item.attr('data-time')).diff(moment()));
            item.text(`Zostało ${duration.days()} dni, ${duration.hours()} godzin ${duration.minutes()} minut, ${duration.seconds()} sekund`);
        });
    }
}
const index = new Index();
$(document).ready(() => {
    index.init();
});