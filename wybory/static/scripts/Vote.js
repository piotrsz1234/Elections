var Vote = /** @class */ (function () {
    function Vote() {
        var _this = this;
        this.init = function () {
            _this.assignControls();
            _this.initControls();
        };
        this.assignControls = function () {
            _this.mainDiv = $('#divVote');
            _this.btnSave = _this.mainDiv.find('[name="btnSave"]');
            _this.txtCaptcha = _this.mainDiv.find('[name="captcha_1"]');
        };
        this.initControls = function () {
            _this.mainDiv.undelegate('input[name="kandydaci"]', 'change').delegate('input[name="kandydaci"]', 'change', function () {
                var allInputs = _this.mainDiv.find('[name="kandydaci"]');
                if (allInputs.is(':checked')) {
                    _this.btnSave.removeClass('disabled');
                }
                else {
                    _this.btnSave.addClass('disabled');
                }
            });
            _this.txtCaptcha.addClass('form-control form-control-sm w-30 mt-2');
            _this.txtCaptcha.attr('placeholder', 'Enter captcha text');
        };
    }
    return Vote;
}());
var vote = new Vote();
$(document).ready(function () {
    vote.init();
});
