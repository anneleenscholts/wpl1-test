// Klein, onopdringerig voorbeeld van JavaScript: geen inline handlers,
// script staat los van de HTML en wordt met "defer" geladen.

document.addEventListener("DOMContentLoaded", () => {
  const stalen = document.querySelectorAll(".kleurstaal");
  const feedback = document.querySelector(".kleur-feedback");

  if (!stalen.length || !feedback) return;

  stalen.forEach((staal) => {
    staal.addEventListener("click", async () => {
      const hex = staal.dataset.hex;

      try {
        await navigator.clipboard.writeText(hex);
        feedback.textContent = `${hex} gekopieerd naar klembord.`;
      } catch (fout) {
        feedback.textContent = `Kopiëren niet gelukt. Hexcode: ${hex}`;
      }
    });
  });
});
