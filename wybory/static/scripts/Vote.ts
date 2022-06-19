class Vote {

    private mainDiv: JQuery;
    private btnSave: JQuery;

    public init = (): void => {
        this.assignControls();
        this.initControls();
    }

    private assignControls = (): void => {
        this.mainDiv = $('#divVote');
        this.btnSave = this.mainDiv.find('[name="btnSave"]');
    }

    private initControls = (): void => {
        this.mainDiv.undelegate('input[name="kandydaci"]', 'change').delegate('input[name="kandydaci"]', 'change', () => {
            const allInputs = this.mainDiv.find('[name="kandydaci"]');
            if(allInputs.is(':checked')) {
                this.btnSave.removeClass('disabled');
            } else {
                this.btnSave.addClass('disabled');
            }
        });
    }
}

const vote = new Vote();
$(document).ready(() => {
    vote.init();
});