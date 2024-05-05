// document.addEventListener("DOMContentLoaded", function () {
//    const imageZooms = document.querySelectorAll(".image-zoom");

//    imageZooms.forEach(function (imageZoom) {
//       imageZoom.addEventListener("mousemove", function (event) {
//          const boundingRect = this.getBoundingClientRect();
//          const offsetX = event.clientX - boundingRect.left;
//          const offsetY = event.clientY - boundingRect.top;
//          const imageWidth = this.offsetWidth;
//          const imageHeight = this.offsetHeight;
//          const mouseXPercent = (offsetX / imageWidth) * 100;
//          const mouseYPercent = (offsetY / imageHeight) * 100;

//          const scaleFactor = 2; // Change this to your desired scale factor
//          const scaleAmount = 1 + (scaleFactor - 1) * 0.5;

//          // Adjust the transform origin based on the mouse position
//          this.style.transformOrigin = `${mouseXPercent}% ${mouseYPercent}%`;

//          // Smoothly zoom the image
//          this.style.transition = "transform 0.2s";
//          this.style.transform = `scale(${scaleAmount})`;
//       });

//       imageZoom.addEventListener("mouseleave", function () {
//          // Reset the zoom when the mouse leaves the image
//          this.style.transition = "transform 0.5s ease";
//          this.style.transform = "scale(1)";
//       });
//    });
// });
document.addEventListener("DOMContentLoaded", function () {
   let lastInteractedCarousel = null; // Variable to store the last interacted carousel

   const imageZooms = document.querySelectorAll(".image-zoom");

   imageZooms.forEach(function (imageZoom) {
      imageZoom.addEventListener("mousemove", function (event) {
         // Track the last interacted carousel
         lastInteractedCarousel = this.parentNode;

         const boundingRect = this.getBoundingClientRect();
         const offsetX = event.clientX - boundingRect.left;
         const offsetY = event.clientY - boundingRect.top;
         const imageWidth = this.offsetWidth;
         const imageHeight = this.offsetHeight;
         const mouseXPercent = (offsetX / imageWidth) * 100;
         const mouseYPercent = (offsetY / imageHeight) * 100;

         const scaleFactor = 2; // Change this to your desired scale factor
         const scaleAmount = 1 + (scaleFactor - 1) * 0.5;

         // Adjust the transform origin based on the mouse position
         this.style.transformOrigin = `${mouseXPercent}% ${mouseYPercent}%`;

         // Smoothly zoom the image
         this.style.transition = "transform 0.2s";
         this.style.transform = `scale(${scaleAmount})`;
      });

      imageZoom.addEventListener("mouseleave", function () {
         // Reset the zoom when the mouse leaves the image
         this.style.transition = "transform 0.5s ease";
         this.style.transform = "scale(1)";
      });
   });

   // Event listener for carousel slide events
   const carouselControls = document.querySelectorAll('.carousel-control-prev, .carousel-control-next');
   carouselControls.forEach(function (control) {
      control.addEventListener('click', function () {
         // Update the last interacted carousel immediately upon control button click
         lastInteractedCarousel = this.closest('.carousel');

         // Stop automatic sliding for all carousels except the last interacted one
         const allCarousels = document.querySelectorAll('.carousel');
         allCarousels.forEach(function (carousel) {
            if (carousel !== lastInteractedCarousel) {
               $(carousel).carousel('pause'); // Stop sliding for carousels except the last interacted one
            }
         });
      });
   });

   // Function to start automatic sliding for the last interacted carousel
   function startAutoSlide() {
      if (lastInteractedCarousel) {
         $(lastInteractedCarousel).carousel('cycle'); // Start sliding for the last interacted carousel
      }
   }

   // Event listener to start automatic sliding when mouse leaves the carousel
   const carousels = document.querySelectorAll('.carousel');
   carousels.forEach(function (carousel) {
      carousel.addEventListener('mouseleave', startAutoSlide); // Start automatic sliding when mouse leaves carousel
   });
});
