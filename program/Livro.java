package program;

public class Livro 
{
    private String isbn;
    private String nome;

    public Livro(String isbn, String nome)
    {
        this.isbn = isbn;
        this.nome = nome;
    }

    public String getISBN()
    {
        return this.isbn;
    }

    public String getNome()
    {
        return this.nome;
    }
}