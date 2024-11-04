import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:math';

void main() {
  runApp(MyApp());
}

List quoteList = [
  "You are poor, you are poor... YOU ARE POOR",
  "I don't need to be motivated because I'm a disciplined person. \nIf I allocate X amount of time to do something, I'm going to do exactly that \nwith complete and absolute vigor for the allocated amount of time.",
  "Every action you take is molding who you are as a person. \nEvery time that you sleep in. \nEvery time you are undisciplined, you are training yourself that it's okay. \nA downward spiral towards mediocrity.",
  "You are exactly where you deserve to be. \nChange who you are \nand you will change how you live.",
  "If I'm not doing something which is either extremely difficult or \nextremely stressful I am in a perpetual state of crippling boredom. \nTherefore I constantly seek difficulty to solve and forever succeed.",
  "Men are not designed to be comfortable. \nThey want to achieve. \nThey want to feel pain and suffering. \nThey want to conquer something.",
  "The person who goes to the gym every day regardless of how they feel \nwill always beat the person who goes to the gym when they feel like going to the gym.",
  "Emotional control isn’t a lack of emotion \nit's a necessary function of maturity",
  "I could never stop fighting even if I lost 100 fights \nbecause I'm not built to live a normal existence",
  "For 12 years I trained 5 hours per day, six days per week \nand I was motivated to train probably 25% of the time. \nThe rest of the time I went because I am disciplined.",
  "You're going to have to work when you don't feel like working. \nThat's how it's going to have to be \nor you're never going to be important.",
  "Sadness is a warning. \nYou feel it for a reason. \nYour mind is telling you that you need to work harder.",
  "The temporary satisfaction of quitting is outweighed \nby the eternal suffering of being a nobody.",
  "Close your eyes. \nFocus on making yourself feel excited, powerful.\nImagine destroying every goal with ease.\nSoon - a smile will appear.\nNow open your eyes.\nGet to work.",
  "The amount of stress you can tolerate while remaining effective \nis directly correlated to the level of success you will enjoy.",
  "If you want people to care about who you are \nbecome familiar with pain.",
  "Being sloppy in one area of your life \nresults in sloppiness in all areas of your life. \nStart with the way you make a cup of coffee \nor the way you handle an argument. \nBe systematic and professional in ALL things.",
  "Success loves speed",
  "Optimism is a prerequisite to genuine efforts",
  "Discipline is the key to success. Absolutely is.",
  "If you cannot force yourself to do something that you do not want to do, \nhow are you ever gonna put yourself through the suffering required for greatness?",
  "I'm very happy that my life has been difficult because it's impossible to become a capable man \nwithout struggling, \nfacing serious adversities, and overcoming insurmountable odds.",
  "People who train every day do \nnot want to train every day. \nThey are not motivated to train every day. \nThey forget motivation and rely on purpose and discipline.",
  "Have you taken advantage of the few things you actually control? \nOr are you still hoping to just get lucky?",
  "My unmatched perspicacity \ncoupled with sheer indefatigability \nmakes me a feared opponent in any realm of human endeavor",
  "You need to understand \nthat in this world there's a whole bunch \nof people doing amazing things that you are not doing \nbecause they're richer than you. \nAnd that needs to piss you off.",
  "Nobody gives a fuck about you as much as you're \ngonna have to give a fuck about yourself.",
  "90% of being successful \nis being able to smile while going through stress, \npain, torment, and bullshit",
  "Think of all of the amazing things you could have accomplished \nby now if you weren't brutally lazy",
  "Make God happy with how hard you work",
  "Today you can act as an amateur or a professional. \nDecide what you will do right now",
  "Maybe you're broke. Maybe you're out of shape. \nMaybe you just want a different life altogether. \nThis 'depression' you feel is the key \nto everything you want to change",
  "Your life can be like a movie. \nYou are the hero. \nBut in every good movie the hero is \nwilling to take risks, are you?",
  "If you truly wanted money, \nyou wouldn't be able to sleep until \nyou fucking had it",
  "If you don't know anybody who is rich, \nyou're not useful to someone who is rich. \nThat's your problem to fix",
  "Money is not the goal, power is. \nOnly power matters in the battle of Good versus Evil.",
  "Poor people like to believe the rich are mysteriously unhappy \nto feel better about being poor",
  "The amount of work you find to do is directly correlated to how much you care. \nWhen you really care about success, the work never ends",
  "You can become rich, you can become strong, \nyou can take care of your loved ones \nand you can enjoy the fact that it will be very difficult to achieve",
  "You will never get rich without a plan. \nStop hoping. Start pla nning",
  "All of life's important lessons come from being broke. \nThe best thing you can hope for as a headstart \nfor a child are: good parents and no money",
];

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        // This is the theme of your application.
        //
        // Try running your application with "flutter run". You'll see the
        // application has a blue toolbar. Then, without quitting the app, try
        // changing the primarySwatch below to Colors.green and then invoke
        // "hot reload" (press "r" in the console where you ran "flutter run",
        // or simply save your changes to "hot reload" in a Flutter IDE).
        // Notice that the counter didn't reset back to zero; the application
        // is not restarted.
        primarySwatch: Colors.blue,
      ),
      home: QuoteGenerator(),
    );
  }
}

class QuoteGenerator extends StatefulWidget {
  const QuoteGenerator({super.key});

  @override
  State<QuoteGenerator> createState() => _QuoteGeneratorState();
}

class _QuoteGeneratorState extends State<QuoteGenerator> {
  final String quoteURL = "https://api.adviceslip.com/advice";
  String quote = 'Success loves speed';

  generateQuote() async {
    // var res = await http.get(Uri.parse(quoteURL));
    // var result = jsonDecode(res.body);
    // print(result["slip"]["advice"]);
    // setState(() {
    //  quote = result["slip"]["advice"];
    //

    int randomIndex = Random().nextInt(quoteList.length);
    var result = quoteList[randomIndex];
    setState(() {
      quote = result;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      appBar: AppBar(
          title: Text('Tate Quote Generator'),
          backgroundColor: Colors.blue[200],
          centerTitle: true),
      drawer: Drawer(
          child: ListView(
        padding: EdgeInsets.zero,
        children: [
          const DrawerHeader(
            decoration: BoxDecoration(
              color: Colors.blue,
            ),
            child: Text('Options'),
          ),
          ListTile(
            title: const Text('Favourites'),
            onTap: () {
              // Update the state of the app.
              // ...
            },
          ),
          ListTile(
            title: const Text('Ordered quotes'),
            onTap: () {
              // Update the state of the app.
              // ...
            },
          ),
          ListTile(
            title: const Text('Random quotes'),
            onTap: () {
              // Update the state of the app.
              // ...
            },
          ),
        ],
      ) // Populate the Drawer in the next step.
          ),
      body: Column(
        children: [
          Expanded(
            child: Align(
              alignment: Alignment.center,
              child: Text(
                quote,
                textAlign: TextAlign.center,
                style: TextStyle(fontSize: 20, color: Colors.white),
              ),
            ),
          ),
          const SizedBox(
            height: 30,
          ),
          Container(
            height: 30,
            width: double.infinity,
            child: Align(
              alignment: Alignment.bottomCenter,
              child: ElevatedButton(
                onPressed: () {
                  generateQuote();
                },
                child: Text('Next Quote'),
              ),
            ),
          ),
          Padding(
            padding: EdgeInsets.only(top: 50.0, bottom: 50.0),
            child: Container(
              height: 40,
              width: double.infinity,
              child: Align(
                alignment: Alignment.center,
                child: TextButton(
                  style: TextButton.styleFrom(foregroundColor: Colors.blue),
                  onPressed: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                          builder: (context) => SequentialWidget()),
                    );
                  },
                  child: const Text('Switch to Ordered Mode'),
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}

class SequentialWidget extends StatefulWidget {
  @override
  _SequentialWidgetState createState() => _SequentialWidgetState();
}

class _SequentialWidgetState extends State<SequentialWidget> {
  int index = 0;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
          title: Text('Tate Quote Generator'),
          backgroundColor: Colors.blue[200],
          centerTitle: true),
      backgroundColor: Colors.black,
      body: Column(
        children: [
          Expanded(
            child: Align(
              alignment: Alignment.center,
              child: Text(
                "Quote " +
                    (index + 1).toString() +
                    ":" +
                    "\n" +
                    quoteList[index],
                textAlign: TextAlign.center,
                style: TextStyle(fontSize: 20, color: Colors.white),
              ),
            ),
          ),
          Container(
            height: 30,
            width: double.infinity,
            child: Align(
              alignment: Alignment.bottomCenter,
              child: ElevatedButton(
                onPressed: () {
                  if (index < quoteList.length - 1) {
                    setState(() {
                      index++;
                    });
                  } else {
                    setState(() {
                      index = 0;
                    });
                  }
                },
                child: Text("Next Quote"),
              ),
            ),
          ),
          Padding(
            padding: EdgeInsets.only(top: 50.0, bottom: 50.0),
            child: Container(
              height: 40,
              width: double.infinity,
              child: Align(
                alignment: Alignment.center,
                child: TextButton(
                    style: TextButton.styleFrom(foregroundColor: Colors.blue),
                    onPressed: () {
                      Navigator.pop(context);
                    },
                    child: Text('Switch to Random Mode')),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
