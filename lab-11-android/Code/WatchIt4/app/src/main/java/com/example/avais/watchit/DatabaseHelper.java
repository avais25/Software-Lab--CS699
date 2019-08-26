package com.example.avais.watchit;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import android.os.Environment;
import android.provider.Settings;
import android.widget.TextView;

import static java.lang.System.out;

/**
 * Created by avais on 21/10/17.
 */

public class DatabaseHelper extends SQLiteOpenHelper
{
    private static final int DATABASE_VERSION=1;
    private static final String DATABASE_NAME="userDetails.db";
    private static final String TABLE_NAME="userDetails";

    private static final String COLUMN_USERNAME="userName";
    private static final String COLUMN_PASSWORD="password";

   // public static final String  DATABASE_FILE_PATH = Environment.getExternalStorageDirectory().toString();

    private static  final String TABLE_CREATE="create table " +TABLE_NAME+" (userName text primary key not null, password text not null);";


    private static final String MOVIE_TABLE_NAME="movieDetails";
    private static final String COLUMN_ID="id";
    private static final String COLUMN_SEATS="seats";
    private static final String COLUMN_MOVIE_NAME="movieName";
    private static final String COLUMN_IMGURL="imgUrl";
    private static final String COLUMN_PRICE="price";


    private static  final String MOVIE_TABLE_CREATE="create table "+MOVIE_TABLE_NAME+" (id int primary key not null , movieName text not null, imgUrl text , seats  int ,price int not  null )";


    SQLiteDatabase db;

    public DatabaseHelper(Context context, String name, SQLiteDatabase.CursorFactory factory, int version) {
        //super(context, DATABADE_NAME, null, DATABASE_VERSION);
        super(context,DATABASE_NAME,null,DATABASE_VERSION);
    }

    public DatabaseHelper(Context context) {
        super(context,DATABASE_NAME, null, DATABASE_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL(TABLE_CREATE);
        db.execSQL(MOVIE_TABLE_CREATE);
       // movieTableInitializer();
        System.out.println("Database created:");
        this.db=db;
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        String query="DROP TABLE IF EXISTS"+TABLE_NAME;
        String query2="DROP TABLE IF EXISTS"+MOVIE_TABLE_NAME;
        db.execSQL(query);
        db.execSQL(query2);
        this.onCreate(db);

    }

    public void movieTableInitializer()
    {

        out.println("Populating movies Database");

        db=this.getWritableDatabase();
        ContentValues values=new ContentValues();
        out.println("before put1");
        values.put(COLUMN_ID,"1");
        out.println("before put2");
        values.put(COLUMN_MOVIE_NAME,"Pursuit of Happyness");
        out.println("before put3");
        values.put(COLUMN_PRICE,"200");

        values.put(COLUMN_SEATS,"150");
        values.put(COLUMN_IMGURL,"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1hlSd2WJer3oyBlJxLpzcp5DOGuxxG7leKzUb18pQd3eNsYT6");

        out.println("before insert");

        db.insert(MOVIE_TABLE_NAME,null,values);

        out.println("Registeration Successful in DatabaseHelper");

        values.put(COLUMN_ID,2);
        values.put(COLUMN_MOVIE_NAME,"October Sky");
        values.put(COLUMN_PRICE,300);
        values.put(COLUMN_SEATS,150);
        values.put(COLUMN_IMGURL,"http://static.tvtropes.org/pmwiki/pub/images/october_sky.jpg");

        db.insert(MOVIE_TABLE_NAME,null,values);

        out.println("Registeration Successful in DatabaseHelper");


        values.put(COLUMN_ID,3);
        values.put(COLUMN_MOVIE_NAME,"A Beautiful Mind");
        values.put(COLUMN_PRICE,400);
        values.put(COLUMN_SEATS,150);
        values.put(COLUMN_IMGURL,"http://2.bp.blogspot.com/-ji3WoNbhLCE/T6kRqShvb1I/AAAAAAAABWk/Rkac-ePcKUM/s1600/61109170_beautifulmind_800x445-thumb-497xauto-2924.jpg");

        db.insert(MOVIE_TABLE_NAME,null,values);

        out.println("Registeration Successful in DatabaseHelper");

        values.put(COLUMN_ID,4);
        values.put(COLUMN_MOVIE_NAME,"Into the Wild");
        values.put(COLUMN_PRICE,500);
        values.put(COLUMN_SEATS,150);
        values.put(COLUMN_IMGURL,"https://i.ytimg.com/vi/lZjUoKhQ-Bw/hqdefault.jpg");

        db.insert(MOVIE_TABLE_NAME,null,values);

        out.println("Registeration Successful in DatabaseHelper");



        db.close();


    }

    public boolean insertUserDetails(UserDetails ud, TextView info)
    {
        db=this.getWritableDatabase();
        ContentValues values=new ContentValues();

        String q="select userName,password from "+TABLE_NAME+";";
        Cursor cursor = db.rawQuery(q, null);
        String a,b;
        b="NA";
        System.out.println("After Query");

        out.println("column index="+cursor.getColumnIndex("userName")+" "+cursor.getColumnIndex("password"));

        if(cursor.moveToFirst())
        {
            do {

                a=cursor.getString(cursor.getColumnIndex("userName"));

                out.println("Do While in search Password "+a);

                if (a.equals(ud.getName()))
                {
                    info.setText("User Name already Exist.");
                    db.close();
                    return false;
                }
            }while (cursor.moveToNext());
        }


        values.put(COLUMN_USERNAME,ud.getName());
        values.put(COLUMN_PASSWORD,ud.getPassword());
        db.insert(TABLE_NAME,null,values);
        out.println("Registeration Successful in DatabaseHelper");
        db.close();
        return true;
    }

    public String searchPassword(String u)
    {
        out.println("Recieved username in search Password "+u);
        db=this.getReadableDatabase();
        String q="select userName,password from "+TABLE_NAME+";";
        Cursor cursor = db.rawQuery(q, null);
        String a,b;
        b="NA";
        System.out.println("After Query");

        out.println("column index="+cursor.getColumnIndex("userName")+" "+cursor.getColumnIndex("password"));

        if(cursor.moveToFirst())
        {
            do {

                a=cursor.getString(cursor.getColumnIndex("userName"));

                out.println("Do While in search Password "+a);

                if (a.equals(u))
                {
                    b=cursor.getString(cursor.getColumnIndex("password"));
                    break;
                }
            }while (cursor.moveToNext());
        }
        return b;
    }


    public String searchSeats(int i)
    {
        String x=String.valueOf(i);
        out.println("Passed value "+x);
        db=this.getReadableDatabase();
        String q="select id,seats from "+MOVIE_TABLE_NAME+";";

        Cursor cursor=db.rawQuery(q,null);
        String a,b="na";

        if(cursor.moveToFirst())
        {
            do {

                a=cursor.getString(cursor.getColumnIndex("id"));

                out.println("Do While in search Seats "+a);

                if (a.equals(x))
                {
                    b=cursor.getString(cursor.getColumnIndex("seats"));
                    break;
                }
            }while (cursor.moveToNext());
        }
        return b;

    }

    public void getPrice(int id,int a)
    {
        out.println("Recieved getPrice "+a);
        db=this.getWritableDatabase();


        db.execSQL("UPDATE "+MOVIE_TABLE_NAME+" SET seats = \'"+a+"\' WHERE id = \'"+id+"\';");

        //Cursor cursor=db.rawQuery(q,null);

        out.println("After sql in getPrice");
        return ;
    }
}
