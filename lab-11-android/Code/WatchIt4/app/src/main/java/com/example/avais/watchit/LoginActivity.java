package com.example.avais.watchit;

import android.content.Intent;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class LoginActivity extends AppCompatActivity {

    DatabaseHelper dh = new DatabaseHelper(this);
    private EditText Name;
    private  EditText Pass;
    private TextView info;
    private TextView err;
    private Button Login;
    private int count=10;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        Name=(EditText)findViewById(R.id.lName);
        Pass= (EditText)findViewById(R.id.lpass);
        info=(TextView) findViewById(R.id.attempts);
        Login=(Button) findViewById(R.id.loginBut);
        err=(TextView)findViewById(R.id.textView2 );

        info.setText("Number of attempts remaining:10");

        Login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                validate(Name.getText().toString(),Pass.getText().toString());
            }
        });


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
    }

    private void validate(String Name, String Pass)
    {


        if((Name.equals("Admin"))&& (Pass.equals("1234") ))
        {
            Intent intent=new Intent(LoginActivity.this,BookActivity2.class);
            startActivity(intent);
            finish();
            return;
        }

        String recPass=dh.searchPassword(Name);
        System.out.println("Recieved Password ="+recPass);
        if(recPass.equals(Pass))
        {
            Intent intent=new Intent(LoginActivity.this,BookActivity2.class);
            startActivity(intent);
            finish();
            return;

        }
        else
        {
            count--;
            if (recPass.equals("NA"))
            {
                err.setText("User Not registered.");
            }
            else
            {
                err.setText("Incorrect Password.");
            }


            info.setText("No of  attempts remaining: "+String.valueOf(count));


            if(count==0)
            {
                Login.setEnabled(false);
            }
        }
    }

    /*@Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.Exit) {
            finish();
            System.exit(0);
            return true;
        }

        return super.onOptionsItemSelected(item);
    }*/

}


