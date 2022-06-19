class Login {
    private mainDiv: JQuery;
    private txtCaptcha: JQuery;

    public init = (): void => {
        this.assignControl();
        this.initControl();
    }

    private assignControl = (): void => {
        this.mainDiv = $('#divLogin');
        this.txtCaptcha = this.mainDiv.find('[name="captcha_1"]');
    }

    private initControl = (): void => {
        this.txtCaptcha.addClass('form-control form-control-sm w-50 mt-2');
        this.txtCaptcha.attr('placeholder', 'Enter captcha text');
    }
}

const login = new Login();
$(document).ready(() => {
    login.init();
})