# json2ofx

I wrote this script to create a very simple minimalistic basic OFX file.

I use the bookkeeping software Xero in the Caribbean. Banks in the Caribbean don't support automatic bank
statement imports (and I want to manage cash and bitcoin as well), so you need to copy bank statements 
manually. But Xero does not allow you to add bank
transactions manually, it only allows you to import CSV and OFX files (and probably a bit more). They 
even provide a CSV template for that, so you can manually create a CSV file. But that's a hassle, and the CSV
format allows you to make too many mistakes. OFX on the other hand, is very structured, strongly typed, and thus
allows for less mistakes.

So, I created this script to manually make a json file, then I run the script, and you get OFX output that you can easily import. I got some inspiration from the OFX files my local banks are creating, your mileage may vary.

## How to run

Just put the example json file in the `inputs.json` file, and run `main.py`. No external libraries needed, so no venv needed as well.

## Example

Consider this input:

    {
      "currency": "ANG",
      "bankid": "BITCOIN",
      "accountid": 0,
      "end_balance": 0,
      "transactions": [
        {
          "date": "20231204",
          "amount": -144.71,
          "name": "Company X",
          "memo": "Invoice 2023-0020"
        },
        {
          "date": "20231204",
          "amount": -2.65,
          "name": "Bitcoin network",
          "memo": "Bank Fee"
        }
      ]
    }

run the script:

	/usr/bin/python3 ~/git/json2ofx/main.py 
	converted 'input.json' to 'output.ofx'


makes for this output:

    <?xml version="1.0" encoding="utf-8"?>
    <?OFX OFXHEADER = "200" VERSION = "202" SECURITY = "NONE" OLDFILEUID = "NONE" NEWFILEUID = "NONE"?>
    <OFX>
      <SIGNONMSGSRSV1>
        <SONRS>
          <STATUS>
            <CODE>0</CODE>
            <SEVERITY>INFO</SEVERITY>
          </STATUS>
          <DTSERVER>20231207153347</DTSERVER>
          <LANGUAGE>ENG</LANGUAGE>
        </SONRS>
      </SIGNONMSGSRSV1>
      <BANKMSGSRSV1>
        <STMTTRNRS>
          <TRNUID>0</TRNUID>
          <STATUS>
            <CODE>0</CODE>
            <SEVERITY>INFO</SEVERITY>
          </STATUS>
          <STMTRS>
            <CURDEF>ANG</CURDEF>
            <BANKACCTFROM>
              <BANKID />
              <ACCTID />
              <ACCTTYPE>CurrentAccount</ACCTTYPE>
            </BANKACCTFROM>
            <BANKTRANLIST>
              <DTSTART>20231204</DTSTART>
              <DTEND>20231204</DTEND>
              <STMTTRN>
                <TRNTYPE>DEBIT</TRNTYPE>
                <DTPOSTED>20231204</DTPOSTED>
                <TRNAMT>-144.71</TRNAMT>
                <FITID>20231204:1276:1</FITID>
                <MEMO>Invoice 2023-0020</MEMO>
                <NAME>Company X</NAME>
              </STMTTRN>
              <STMTTRN>
                <TRNTYPE>DEBIT</TRNTYPE>
                <DTPOSTED>20231204</DTPOSTED>
                <TRNAMT>-2.65</TRNAMT>
                <FITID>20231204:5288:1</FITID>
                <MEMO>Bank Fee</MEMO>
                <NAME>Bitcoin network</NAME>
              </STMTTRN>
            </BANKTRANLIST>
            <LEDGERBAL>
              <BALAMT>0</BALAMT>
              <DTASOF>20231207</DTASOF>
            </LEDGERBAL>
          </STMTRS>
        </STMTTRNRS>
      </BANKMSGSRSV1>
    </OFX>

## Considerations

As you may have noticed you will probably want to change the currency from ANG to USD or EUR, perhaps you want to set some accountid (perhaps the bank account number?), and if you study the OFX standard you'll see there's a lot of other fields you can add!

You can see a field called FITID per transaction line, that has a unique identifier to identify duplicate transactions. I just generate that id by generating a hash of the transaction. Perhaps your situation calls for something differen!