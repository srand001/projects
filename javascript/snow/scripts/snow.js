function renderSnowContainer() {
  const snowContainer = document.createElement('div');
  snowContainer.id = 'snow-container';

  document.body.appendChild(snowContainer);

  return snowContainer;
}

const flakeImages = [
  'images/flake.png',
  'images/flake2.png',
  'images/flake3.png',
];

function renderFlake(snowContainer) {
  const flakeContainer = document.createElement('div');
  flakeContainer.classList.add('flake-container');

  flakeContainer.style.left = `${Math.random() * 100}%`;
  flakeContainer.style.transform = `scale(${Math.random()})`;

  const img = document.createElement('img');
  img.src = flakeImages[Math.floor(Math.random() * flakeImages.length)];

  if (Math.floor(Math.random() * 6) < 3) {
    img.style.filter = "brightness(175%) contrast(175%)";
  } else {
    img.style.filter = "brightness(125%) contrast(125%)";
  }

  flakeContainer.appendChild(img);

  snowContainer.appendChild(flakeContainer);

  setTimeout(renderFlake, 100, snowContainer);
}

function addAudioElement(snowContainer) {
  const audioElement = document.createElement('audio');
  audioElement.src = 'sounds/jinglebells.mp3';
  audioElement.play();

  snowContainer.appendChild(audioElement);
}

const snowContainer = renderSnowContainer();

  renderFlake(snowContainer);
  addAudioElement(snowContainer);

  { once: true }

