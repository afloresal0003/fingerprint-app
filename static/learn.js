document.addEventListener("DOMContentLoaded", function () {
   const imageZooms = document.querySelectorAll(".image-zoom");

   imageZooms.forEach(function (imageZoom) {
      imageZoom.addEventListener("mousemove", function (event) {
         const boundingRect = this.getBoundingClientRect();
         const offsetX = event.clientX - boundingRect.left;
         const offsetY = event.clientY - boundingRect.top;
         const imageWidth = this.offsetWidth;
         const imageHeight = this.offsetHeight;
         const mouseXPercent = (offsetX / imageWidth) * 100;
         const mouseYPercent = (offsetY / imageHeight) * 100;
         const scaleFactor = 2; // Change this to your desired scale factor

         // Adjust the transform origin based on the scale factor
         const adjustedScaleFactor = Math.min(scaleFactor, 1 + (scaleFactor - 1) * 0.5);
         this.style.transformOrigin = `${mouseXPercent}% ${mouseYPercent}%`;

         // Adjust the transition duration based on the scale factor
         const transitionDuration = 0.5 / adjustedScaleFactor;
         this.style.transitionDuration = `${transitionDuration}s`;
      });
   });
});
