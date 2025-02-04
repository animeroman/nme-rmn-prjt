const slider = document.querySelector('#slick-home-wrapper');

let isDown = false;
let startX,
  scrollLeft,
  lastX,
  velocity = 0,
  momentumID,
  isDragging = false;
const friction = 0.98; // Adjust for smoother/slower momentum
const minVelocity = 0.6; // Threshold to stop momentum

// Disable CSS smooth scroll for better JS control
slider.style.scrollBehavior = 'auto';

function applyMomentum() {
  if (Math.abs(velocity) > minVelocity) {
    slider.scrollLeft -= velocity;
    velocity *= friction; // Apply friction to slow down gradually
    momentumID = requestAnimationFrame(applyMomentum);
  } else {
    cancelAnimationFrame(momentumID);
  }
}

slider.addEventListener('mousedown', e => {
  isDown = true;
  startX = e.pageX - slider.offsetLeft;
  lastX = startX;
  scrollLeft = slider.scrollLeft;
  velocity = 0;
  isDragging = false;
  cancelAnimationFrame(momentumID); // Stop previous momentum
});

slider.addEventListener('mouseleave', () => {
  if (isDown) applyMomentum();
  isDown = false;
});

slider.addEventListener('mouseup', () => {
  if (isDown) applyMomentum();
  isDown = false;
});

slider.addEventListener('mousemove', e => {
  if (!isDown) return;
  e.preventDefault();
  const x = e.pageX - slider.offsetLeft;
  const walk = x - startX; // Adjust scroll speed
  velocity = x - lastX; // Calculate velocity based on movement
  lastX = x;
  slider.scrollLeft = scrollLeft - walk;

  if (Math.abs(walk) > 5) {
    isDragging = true;
  }
});

// Prevent accidental clicks when dragging
slider.addEventListener('click', e => {
  if (isDragging) {
    e.preventDefault();
    e.stopPropagation();
  }
});

// --- Touch Support with Momentum ---
slider.addEventListener('touchstart', e => {
  isDown = true;
  startX = e.touches[0].pageX - slider.offsetLeft;
  lastX = startX;
  scrollLeft = slider.scrollLeft;
  velocity = 0;
  isDragging = false;
  cancelAnimationFrame(momentumID);
});

slider.addEventListener('touchmove', e => {
  if (!isDown) return;
  const x = e.touches[0].pageX - slider.offsetLeft;
  const walk = x - startX;
  velocity = x - lastX;
  lastX = x;
  slider.scrollLeft = scrollLeft - walk;

  if (Math.abs(walk) > 5) {
    isDragging = true;
  }
});

slider.addEventListener('touchend', () => {
  if (isDown) applyMomentum();
  isDown = false;
});
