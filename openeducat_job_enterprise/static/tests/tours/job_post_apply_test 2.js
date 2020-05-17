odoo.define('openeducat_job_enterprise.tour', function (require) {
'use strict';

var tour = require("web_tour.tour");

tour.register('test_job_apply', {
    test: true,
    url: '/job/post/apply/1',
},
    [
        {
            content: "Add new Job Position",
            trigger: 'form[action^="/form/submit"]',
        },
    ]
);

});
