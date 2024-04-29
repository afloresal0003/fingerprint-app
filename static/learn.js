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
});
