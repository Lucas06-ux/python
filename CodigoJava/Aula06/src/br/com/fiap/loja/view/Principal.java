package br.com.fiap.loja.view;


import br.com.fiap.loja.model.Cliente;

public class Principal {
    public static void main(String[] args) {


        Cliente cliente = new Cliente("Lucas", 18, "2732782392" , true);


        System.out.println("Seu nome é: " + cliente.getNome());
        System.out.println("Sua idade é: " + cliente.getIdade());
        System.out.println("Seu telefone é: " + cliente.getTelefone());
        System.out.println(cliente.isVip());

    }
}
