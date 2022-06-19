class Vote {

    private mainDiv: JQuery;
    private btnSave: JQuery;
    private txtCaptcha: JQuery;

    public init = (): void => {
        this.assignControls();
        this.initControls();
    }

    private assignControls = (): void => {
        this.mainDiv = $('#divVote');
        this.btnSave = this.mainDiv.find('[name="btnSave"]');
        this.txtCaptcha = this.mainDiv.find('[name="captcha_1"]');
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
        this.txtCaptcha.addClass('form-control form-control-sm w-30 mt-2');
        this.txtCaptcha.attr('placeholder', 'Enter captcha text');
    }
}

const vote = new Vote();
$(document).ready(() => {
    vote.init();
});