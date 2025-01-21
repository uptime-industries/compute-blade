"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.DEFAULT_OPTIONS = void 0;
exports.validateOptions = validateOptions;
exports.validateThemeConfig = validateThemeConfig;
const utils_validation_1 = require("@docusaurus/utils-validation");
exports.DEFAULT_OPTIONS = {
    async: false,
    defer: false
};
const pluginOptionsSchema = utils_validation_1.Joi.object({
    accountId: utils_validation_1.Joi.alternatives()
        .try(utils_validation_1.Joi.alternatives().conditional(utils_validation_1.Joi.number().required(), {
        then: utils_validation_1.Joi.custom((val) => [val]),
    }), utils_validation_1.Joi.array().items(utils_validation_1.Joi.number().required()))
        .required(),
    async: utils_validation_1.Joi.boolean().default(exports.DEFAULT_OPTIONS.async),
    defer: utils_validation_1.Joi.boolean().default(exports.DEFAULT_OPTIONS.defer),
});
function validateOptions({ validate, options, }) {
    return validate(pluginOptionsSchema, options);
}
function validateThemeConfig({ themeConfig, }) {
    if ('hubspot' in themeConfig) {
        throw new Error('The "hubspot" field in themeConfig should now be specified as option in plugins.');
    }
    return themeConfig;
}
