var Login = /** @class */ (function () {
    function Login() {
        var _this = this;
        this.init = function () {
            _this.assignControl();
            _this.initControl();
        };
        this.assignControl = function () {
            _this.mainDiv = $('#divLogin');
            _this.txtCaptcha = _this.mainDiv.find('[name="captcha_1"]');
        };
        this.initControl = function () {
            _this.txtCaptcha.addClass('form-control form-control-sm w-50 mt-2');
            _this.txtCaptcha.attr('placeholder', 'Enter captcha text');
        };
    }
    return Login;
}());
var login = new Login();
$(document).ready(function () {
    login.init();
});
