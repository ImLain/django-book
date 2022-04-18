window.onload = () => {
    // On va chercher toutes les étoiles
    const stars = document.querySelectorAll(".la-star");
   
    // On va chercher l'input
    const score = document.querySelector("#id_score"); //mettre "score"
 
    // On boucle sur les étoiles pour leur ajouter des écouteurs d'évènements
    for(star of stars){
        // On écoute le survol
        star.addEventListener("mouseover", function(){
            resetStars();
            this.style.color = "red";
            this.classList.add("las"); // pour remplir l'étoile de rouge repris dans le while
            this.classList.remove("lar");// pour rendre l'étoile vide
            // L'élément précédent dans le DOM (de même niveau, balise soeur)
            let previousStar = this.previousElementSibling;
 
            while(previousStar){
                // On passe l'étoile qui précède en rouge
                previousStar.style.color = "red";
                previousStar.classList.add("las");
                previousStar.classList.remove("lar");
                // On récupère l'étoile qui la précède
                previousStar = previousStar.previousElementSibling;
            }
        });
 
        // On écoute le clic
        star.addEventListener("click", function(){
            score.value = this.dataset.value; // mettre score.value
        });
 
                // permet de conserver les étoiles où on a passé la souris
        star.addEventListener("mouseout", function(){
            resetStars(score.value); //  mettre score.value
        });
    }
 
    /**
     * Reset des étoiles en vérifiant la note dans l'input caché
     * @param {number} score 
     */
    function resetStars(score = 0){  // mettre score
        for(star of stars){
            if(star.dataset.value > score){ // mettre score
                star.style.color = "black";
                star.classList.add("lar");
                star.classList.remove("las");
            }else{
                star.style.color = "red";
                star.classList.add("las");
                star.classList.remove("lar");
            }
        }
    }
}