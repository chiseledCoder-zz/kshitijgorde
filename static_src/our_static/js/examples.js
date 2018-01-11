/* Examples */
(function($) {
  /*
   * Example 1:
   *
   * - no animation
   * - custom gradient
   *
   * By the way - you may specify more than 2 colors for the gradient
   */

  /*
   * Example 2:
   *
   * - default gradient
   * - listening to `circle-animation-progress` event and display the animation progress: from 0 to 100%
   */
  $('.second.circle').circleProgress({
    value: 0.9
  }).on('circle-animation-progress', function(event, progress) {
    $(this).find('strong').html(Math.round(90 * progress) + '<i>%</i>');
  });
  $('.leadership.circle').circleProgress({
    value: 0.8
  }).on('circle-animation-progress', function(event, progress) {
    $(this).find('strong').html(Math.round(80 * progress) + '<i>%</i>');
  });
  $('.speaking.circle').circleProgress({
    value: 0.7
  }).on('circle-animation-progress', function(event, progress) {
    $(this).find('strong').html(Math.round(70 * progress) + '<i>%</i>');
  });
  $('.team.circle').circleProgress({
    value: 0.6
  }).on('circle-animation-progress', function(event, progress) {
    $(this).find('strong').html(Math.round(60 * progress) + '<i>%</i>');
  });
  $('.second.english.circle').circleProgress({
    value: 0.95
  }).on('circle-animation-progress', function(event, progress) {
    $(this).find('strong').html(Math.round(95 * progress) + '<i>%</i>');
  });
  $('.second.spanish.circle').circleProgress({
    value: 0.85
  }).on('circle-animation-progress', function(event, progress) {
    $(this).find('strong').html(Math.round(85 * progress) + '<i>%</i>');
  });
  $('.second.french.circle').circleProgress({
    value: 0.7
  }).on('circle-animation-progress', function(event, progress) {
    $(this).find('strong').html(Math.round(70 * progress) + '<i>%</i>');
  });

  /*
   * Example 3:
   *
   * - very custom gradient
   * - listening to `circle-animation-progress` event and display the dynamic change of the value: from 0 to 0.8
   */
  /*
   * Example 4:
   *
   * - solid color fill
   * - custom start angle
   * - custom line cap
   * - dynamic value set
   */

  // Let's emulate dynamic value update
  /*
   * Example 5:
   *
   * - image fill; image should be squared; it will be stretched to SxS size, where S - size of the widget
   * - fallback color fill (when image is not loaded)
   * - custom widget size (default is 100px)
   * - custom circle thickness (default is 1/14 of the size)
   * - reverse drawing mode
   * - custom animation start value
   * - usage of "data-" attributes
   */
  $('.fifth.circle').circleProgress({
    value: 0.7
    // all other config options were taken from "data-" attributes
    // options passed in config object have higher priority than "data-" attributes
    // "data-" attributes are taken into account only on init (not on update/redraw)
    // "data-fill" (and other object options) should be in valid JSON format
  });
})(jQuery);
