
<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="factorial"/>
        <attribute name="authors" value="CENTIC"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2024-08-22 09:42:10 a.&#160;m."/>
        <attribute name="created" value="Q0VOVElDOzItNS0yMDsyMDI0LTA4LTIyOzA5OjEwOjU3IGEuwqBtLjsyMzE2"/>
        <attribute name="edited" value="Q0VOVElDOzItNS0yMDsyMDI0LTA4LTIyOzA5OjQyOjEwIGEuwqBtLjsyOzI0MTk="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <comment text="factorial 22/08/2024"/>
            <declare name="n, x, y" type="Integer" array="False" size=""/>
            <input variable="n"/>
            <assign variable="x" expression="1"/>
            <assign variable="y" expression="1"/>
            <while expression="y&lt;=n">
                <comment text="El x lo usamos para ir guardando el resultado de multiplicar y(y+1) n veces"/>
                <assign variable="x" expression="x*y"/>
                <comment text="Asi, y se multiplica por si mismo mas 1 hasta llegar a n, cuando pasa esto, obtenemos el resultado"/>
                <assign variable="y" expression="y+1"/>
            </while>
            <output expression="x" newline="True"/>
        </body>
    </function>
</flowgorithm>