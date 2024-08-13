const shareButton = document.getElementById("share-button");
shareButton.addEventListener("click", () => {
  const currentUrl = window.location.href;
  const tooltip = document.getElementById("copied-tip");
  navigator.clipboard.writeText(currentUrl);
  tooltip.classList.remove("hidden");
  setTimeout(() => {
    tooltip.classList.add("hidden");
  }, 1500);
});

const homeButton = document.getElementById("home-button");
homeButton.addEventListener("click", () => {
  window.location.href = "../../";
});
