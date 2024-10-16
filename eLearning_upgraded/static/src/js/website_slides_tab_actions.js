/** @odoo-module **/
odoo.define('eLearning_upgraded.website_slides_tab_actions', [], function (require) {
    "use strict";

    $(document).ready(function () {
        // Handle button/link click
        $(document).on('click', '.add_review', function () {

              //  Define the tab we want to visit
              const newActiveTab = 'review'; // Change to "Reviews" tab

              // Remove 'active' and aria-selected='true' from current tab
              $('.nav-link.active').removeClass('active').attr('aria-selected', 'false');

              // Add 'active' and aria-selected='true' to new tab
              const $newActiveLink = $(`#${newActiveTab}-tab`);
              $newActiveLink.addClass('active').attr('aria-selected', 'true');

              // Show the new tab content
              $('.tab-pane').removeClass('show active');
              $(`#${newActiveTab}`).addClass('show active');

              //Hide side review div
              $('#display_review_div').addClass('d-none');
        });

        // Handle tab click
        $(document).on('click', '.custom_wslides_course_main .o_wslides_nav_tabs .nav-link', function (event) {
            const activeTab = $(event.currentTarget).attr('id');

            if (activeTab === 'review-tab') {
                $('#display_review_div').addClass('d-none');  // Show the div 
            } else {
                $('#display_review_div').removeClass('d-none');  // Hide the div
            }
      });
    });

});
