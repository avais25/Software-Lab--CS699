package com.example.avais.watchit;

import android.content.Intent;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import static java.lang.System.out;

public class BookActivity2 extends AppCompatActivity {


    DatabaseHelper dh = new DatabaseHelper(this);


    private EditText Seats1;
    private TextView info1;
    private EditText Seats2;
    private TextView info2;
    private EditText Seats3;
    private TextView info3;
    private EditText Seats4;
    private TextView info4;
    private Button Book;

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        out.println("Book Activity 2started");

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_book2);

        Seats1=(EditText)findViewById(R.id.editTextSeats1);
        info1=(TextView) findViewById(R.id.textViewSeats1);
        Seats2=(EditText)findViewById(R.id.editTextSeats2);
        info2=(TextView) findViewById(R.id.textViewSeats2);
        Seats3=(EditText)findViewById(R.id.editTextSeats3);
        info3=(TextView) findViewById(R.id.textViewSeats3);
        Seats4=(EditText)findViewById(R.id.editTextSeats4);
        info4=(TextView) findViewById(R.id.textViewSeats4);

        Book=(Button) findViewById(R.id.bookButton);

        String[] recv=new String[5];
        for (int i=1;i<=4;i++)
        {
            recv[i]=dh.searchSeats(i);

        }
        info1.setText("Seats: "+recv[1]);
        info2.setText("Seats: "+recv[2]);
        info3.setText("Seats: "+recv[3]);
        info4.setText("Seats: "+recv[4]);








        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        getSupportActionBar().setTitle("Watch It!");

        /*FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                        .setAction("Action", null).show();
            }
        });*/

        out.println("Last line of onCrete booking");
    }

    public void bookNow(View v)
    {
        Seats1=(EditText)findViewById(R.id.editTextSeats1);
        info1=(TextView) findViewById(R.id.textViewSeats1);
        Seats2=(EditText)findViewById(R.id.editTextSeats2);
        info2=(TextView) findViewById(R.id.textViewSeats2);
        Seats3=(EditText)findViewById(R.id.editTextSeats3);
        info3=(TextView) findViewById(R.id.textViewSeats3);
        Seats4=(EditText)findViewById(R.id.editTextSeats4);
        info4=(TextView) findViewById(R.id.textViewSeats4);



        Book=(Button) findViewById(R.id.bookButton);

        //bundle
        Bundle bundle = new Bundle();


        String[] recv=new String[5];
        for (int i=1;i<=4;i++)
        {
            recv[i]=dh.searchSeats(i);

        }
        int[] s=new int[5];
        out.println("After all searchSeats");

        try {

            if (Seats1.getText().toString().equals(""))
            {
                s[1]=0;
            }
            else
            {
                s[1] = Integer.parseInt(Seats1.getText().toString());
             }

            if (Seats2.getText().toString().equals(""))
            {
                s[2]=0;
            }
            else
            {
                s[2] = Integer.parseInt(Seats2.getText().toString());
            }

            if (Seats3.getText().toString().equals(""))
            {
                s[3]=0;
            }
            else
            {
                s[3] = Integer.parseInt(Seats3.getText().toString());
            }

            if (Seats4.getText().toString().equals(""))
            {
                s[4]=0;
            }
            else
            {
                s[4] = Integer.parseInt(Seats4.getText().toString());
            }


        }
        catch (NumberFormatException e)
        {
            bundle.putString("content" , "error");
            Intent intent=new Intent(BookActivity2.this,BookingStatus.class);
            intent.putExtras(bundle);
            startActivity(intent);
            finish();

            return;
        }
        out.println("After parsing to int"+s[1]+" "+s[2]+" "+s[3]+" "+s[4]);
        int[] fin=new int[5];
        out.println("Before calculating fin");
        fin[1]=Integer.parseInt(recv[1])-s[1];
        fin[2]=Integer.parseInt(recv[2])-s[2];
        fin[3]=Integer.parseInt(recv[3])-s[3];
        fin[4]=Integer.parseInt(recv[4])-s[4];


        for(int i=1;i<=4;i++)
        {
            if (fin[i]<0)
            {
                bundle.putString("content" , "error");
                Intent intent=new Intent(BookActivity2.this,BookingStatus.class);
                intent.putExtras(bundle);
                startActivity(intent);
                finish();
                return;
            }
        }

        int price=0;
        int cc=200;

        for (int j=1;j<=4;j++)
        {

            if (s[j]>0)
            {
                dh.getPrice(j,fin[j]);
                price=price+(cc*s[j]);

            }
            cc=cc+100;



        }

        out.println("Tota price="+price);


        bundle.putString("content" , Integer.toString(price));
        Intent intent=new Intent(BookActivity2.this,BookingStatus.class);
        intent.putExtras(bundle);

        startActivity(intent);
        finish();




    }

}
