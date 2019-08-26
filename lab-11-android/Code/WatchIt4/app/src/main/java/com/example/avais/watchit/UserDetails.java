package com.example.avais.watchit;

/**
 * Created by avais on 21/10/17.
 */

public class UserDetails {
    String userName,password;



    public void  setName(String name)
    {
        this.userName=name;
    }

    public String getName()
    {
        return this.userName;
    }

    public void  setPassword(String pass)
    {
        this.password=pass;
    }

    public String getPassword()
    {
        return this.password;
    }

}
