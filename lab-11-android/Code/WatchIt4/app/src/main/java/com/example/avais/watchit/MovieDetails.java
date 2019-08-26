package com.example.avais.watchit;

/**
 * Created by avais on 22/10/17.
 */

public class MovieDetails {
    String movieName, imgUrl;
    int id,seats,price;

    public void  setMovieName(String name)
    {
        this.movieName=name;
    }

    public String getMovieName()
    {
        return this.movieName;
    }

    public void  setImgUrl(String url)
    {
        this.imgUrl=url;
    }

    public String getImgUrl()
    {
        return this.imgUrl;
    }

    public void  setId(int i)
    {
        this.id=i;
    }

    public int getId()
    {
        return this.id;
    }

    public void  setSeats(int s)
    {
        this.seats=s;
    }

    public int getSeats()
    {
        return this.seats;
    }

    public void  setPrice(int name)
    {
        this.price=name;
    }

    public int getPrice()
    {
        return this.price;
    }


}
