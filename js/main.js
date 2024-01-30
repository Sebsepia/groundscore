$(document).ready(function () {
  $(function(){
    $("#navigator").load("navigation.html");
  });



  $('#menutoggle').click(function()  {
   $('.menu').toggleClass('switch');
  });
  
 
  
  // Array of HTML files you want to load
  const sketchbookFiles = [
    'sketchbooks/2021-gris.html',
    'sketchbooks/2020-kaki.html',
    'sketchbooks/2020-watercolor.html',
    'sketchbooks/2020-rose.html',
    'sketchbooks/2019-moleskine.html',
    'sketchbooks/2018-moleskine.html',
    'sketchbooks/2017-kaki.html',
      // Add more files if you want
  ];
  // Iterate through the array and load each HTML file
  $.each(sketchbookFiles, function(index, file) {
      // Load the HTML content and append it to the body
      $.get(file, function(data) {
          $('.sketchbooks').append(data);
      });
  });

      var digital_src = 'art/digital_src.html';

      // Specify the div class
      var digital = '.digital';
  
      // Check if the div with the specified class exists
      if ($(digital).length) {
          // Load HTML content into the div
        $(digital).prepend($('<div>')).load(digital_src, function(response, status, xhr) {
              if (status === "error") {
                  console.log('Error loading HTML file');
              }
          });
      }
      var traditional_src = 'art/traditional_src.html';

      // Specify the div class
      var traditional = '.traditional';
  
      // Check if the div with the specified class exists
      if ($(traditional).length) {
          // Load HTML content into the div
          $(traditional).load(traditional_src, function(response, status, xhr) {
              if (status === "error") {
                  console.log('Error loading HTML file');
              }
          });
      }
      var photo_src = 'art/photo_src.html';

      // Specify the div class
      var photo = '.photo';
  
      // Check if the div with the specified class exists
      if ($(photo).length) {
          // Load HTML content into the div
          $(photo).load(photo_src, function(response, status, xhr) {
              if (status === "error") {
                  console.log('Error loading HTML file');
              }
          });
      }




});

$(document).ready(function() {
  // Delegate the click event to the body for dynamically loaded content
  $('body').on('click', '.sketchbook_cover', function() {
      $(this).siblings().toggleClass('switch');
  });   

  // Delegate the click event to the body for dynamically loaded content
  $('body').on('click', '.sketchbook .sketchbook_page', function(e) {
      e.stopPropagation();
  });



});


