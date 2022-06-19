//import * as moment from 'moment'

class Index {
    public init = (): void => {
        setInterval(this.calcAllTimes, 1000);
    }

    private calcAllTimes = () : void => {
        let elems = $('.sp-calc-time[data-time]');
        elems.each((index: number, Elem: Element) => {
            const item = $(Elem);
            const timeLeft = moment(moment(item.attr('data-time')).diff(moment()));
            item.text(`Zostało ${timeLeft.format('d')} dni, ${timeLeft.format('h')} godzin ${timeLeft.format('mm')} minut, ${timeLeft.format('ss')} sekund`);
        });
    }
}
const index = new Index();
$(document).ready(() => {
    index.init();
});