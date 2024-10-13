const listaSelecaoPokedevs = document.querySelectorAll(".pokedev");


listaSelecaoPokedevs.forEach(pokedev => {
    pokedev.addEventListener("click", () => {
        const cartaoPokedevAberto = document.querySelector(".aberto");
        cartaoPokedevAberto.classList.remove("aberto");


        const idSelecionado = pokedev.attributes.id.value;
        const idDoCartaoParaAbrir = "cartao-" + idSelecionado
        const cartaoParaAbrir = document.getElementById(idDoCartaoParaAbrir);
        cartaoParaAbrir.classList.add("aberto");



        const listaCartaoPokedev = document.querySelector(".ativo");
        listaCartaoPokedev.classList.remove("ativo");

        const idDoCartaoListaParaAbrir = document.getElementById(idSelecionado);
        idDoCartaoListaParaAbrir.classList.add("ativo");



    })
})