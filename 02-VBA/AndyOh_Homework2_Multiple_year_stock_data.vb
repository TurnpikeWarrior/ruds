' ============================================
' Unit 2 | Assignment - The VBA of Wall Street
' Andy Oh
' ============================================

Sub stock()

'Look through all worksheets
  For Each ws In Worksheets

'Declaring all variables and initializing them with 0
    Dim TickerName As String 'Ticker Symbol

    Dim TickerTotal As Double 'Total Trade Volume for each stock
    TickerTotal = 0
 
    Dim Summary_Table_Row As Integer 'Total Rows of the table
    Summary_Table_Row = 2
 
    Dim Counter As Double 'Loop Counter
    Counter = 0

    Dim StartingPrice As Double 'Opening Price
    Dim EndingPrice As Double 'Closing Price
    Dim YearlyChange As Double 'Yearly Change from the stock price at the beginning of the year to the price at the end of the year
    Dim PercentChange As Double 'Percent Change in that stock’s price from the beginning of the year to the end
    Dim MaxValue As Double 'Greatest % Increase
    Dim MinValue As Double 'Greatest % Decrease

    Dim lastRow As Long 'Determine the Last Row
    lastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row

    Dim lastVal As Long
    lastVal = ws.Cells(Rows.Count, "K").End(xlUp).Row

    Dim k As Long
    Dim GTV as Double 

'Setting up Table with additional columns
    ws.Range("I1").Value = "Ticker"
    ws.Range("J1").Value = "Yearly Change"
    ws.Range("K1").Value = "Percent Change"
    ws.Range("L1").Value = "Total Stock Volume"
    ws.Range("O2").Value = "Greatest % Increase"
    ws.Range("O3").Value = "Greatest % Decrease"
    ws.Range("O4").Value = "Greatest Total Volume"
    ws.Range("P1").Value = "Ticker"
    ws.Range("Q1").Value = "Value"

'Setting up Formulas
    For i = 2 To lastRow
      If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then
        TickerName = ws.Cells(i, 1).Value
        TickerTotal = TickerTotal + ws.Cells(i, 7).Value
        StartingPrice = ws.Cells(i - Counter, 6).Value
        EndingPrice = ws.Cells(i, 6).Value
        YearlyChange = EndingPrice - StartingPrice
        PercentChange = (YearlyChange / StartingPrice)

'Checking if Yearly Change increased (green) or decreased (red)
        If YearlyChange < 0 Then
          ws.Range("J" & Summary_Table_Row).Interior.ColorIndex = 3
        Else
          ws.Range("J" & Summary_Table_Row).Interior.ColorIndex = 4
        End If

'Print all results
        ws.Range("I" & Summary_Table_Row).Value = TickerName
        ws.Range("J" & Summary_Table_Row).Value = YearlyChange
        ws.Range("K" & Summary_Table_Row).Value = PercentChange
        ws.Range("K" & Summary_Table_Row).NumberFormat = "0.00%"
        ws.Range("L" & Summary_Table_Row).Value = TickerTotal
        
'End of Loop and Resetting the variables
        Summary_Table_Row = Summary_Table_Row + 1
        TickerTotal = 0
        StartingPrice = 0
        EndingPrice = 0
        PercentChange = 0
        YearlyChange = 0
      Else
'Continue Looping
        TickerTotal = TickerTotal + ws.Cells(i, 7).Value
        Counter = Counter + 1
      End If
    Next i

'Finding Greatest % Increase
    MaxValue = ws.Application.Max(Range("K:K"))
    ws.Range("Q2").Value = MaxValue
    ws.Range("Q2").NumberFormat = "0.00%"
    
    For k = 2 To lastVal
      If ws.Range("K" & k).Value = MaxVal Then
        ws.Range("P2").Value = ws.Range("I" & k).Value
      End If
    Next k

'Finding Greatest % Decrease
    MinValue = ws.Application.Min(Range("K:K"))
    ws.Range("Q3").Value = MinValue
    ws.Range("Q3").NumberFormat = "0.00%"

    For k = 2 To lastVal
      If ws.Range("K" & k).Value = MinVal Then
        ws.Range("P3").Value = ws.Range("I" & k).Value
      End If
    Next k

'Finding Greatest Total Volume
    GTV = ws.Application.Max(Range("L:L"))
    ws.Range("Q4").Value = GTV

    For k = 2 To lastVal
      If ws.Range("L" & k).Value = GTV Then
        ws.Range("P4").Value = ws.Range("I" & k).Value
      End If
    Next k

    ' ws.Columns("A:Q").EntireColumn.AutoFit
  Next ws

'END OF PROGRAM
    MsgBox ("Process Completed")
End Sub