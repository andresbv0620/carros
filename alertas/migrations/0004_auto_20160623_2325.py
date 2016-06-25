# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 23:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('alertas', '0003_auto_20160621_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='price_max',
            field=models.CharField(blank=True, choices=[(None, 'Hasta'), ('5000000', '5.000.000'), ('10000000', '10.000.000'), ('15000000', '15.000.000'), ('20000000', '20.000.000'), ('25000000', '25.000.000'), ('30000000', '30.000.000'), ('35000000', '35.000.000'), ('40000000', '40.000.000'), ('45000000', '45.000.000'), ('50000000', '50.000.000'), ('55000000', '55.000.000'), ('60000000', '60.000.000'), ('70000000', '70.000.000'), ('80000000', '80.000.000'), ('100000000', '100.000.000'), ('120000000', '120.000.000'), ('-1', 'Mas de 120.000.000')], default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='alert',
            name='price_min',
            field=models.CharField(blank=True, choices=[(None, 'Desde'), ('-1', 'Menos de 5.000.000'), ('5000000', '5.000.000'), ('10000000', '10.000.000'), ('15000000', '15.000.000'), ('20000000', '20.000.000'), ('25000000', '25.000.000'), ('30000000', '30.000.000'), ('35000000', '35.000.000'), ('40000000', '40.000.000'), ('45000000', '45.000.000'), ('50000000', '50.000.000'), ('55000000', '55.000.000'), ('60000000', '60.000.000'), ('70000000', '70.000.000'), ('80000000', '80.000.000'), ('100000000', '100.000.000'), ('120000000', '120.000.000')], default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='alert',
            name='year_max',
            field=models.CharField(blank=True, choices=[(None, 'Hasta'), ('2017', '2017'), ('2016', '2016'), ('2015', '2015'), ('2014', '2014'), ('2013', '2013'), ('2012', '2012'), ('2011', '2011'), ('2010', '2010'), ('2009', '2009'), ('2008', '2008'), ('2007', '2007'), ('2006', '2006'), ('2005', '2005'), ('2004', '2004'), ('2003', '2003'), ('2002', '2002'), ('2001', '2001'), ('2000', '2000'), ('1999', '1999'), ('1998', '1998'), ('1997', '1997'), ('1996', '1996'), ('1995', '1995'), ('1994', '1994'), ('1993', '1993'), ('1992', '1992'), ('1991', '1991'), ('1990', '1990'), ('1989', '1989'), ('1988', '1988'), ('1987', '1987'), ('1986', '1986'), ('1985', '1985'), ('1984', '1984'), ('1983', '1983'), ('1982', '1982'), ('1981', '1981'), ('1980', '1980'), ('1979', '1979'), ('1978', '1978'), ('1977', '1977'), ('1976', '1976'), ('1975', '1975'), ('1974', '1974'), ('1973', '1973'), ('1972', '1972'), ('1971', '1971'), ('1970', '1970'), ('1969', '1969'), ('1968', '1968'), ('1967', '1967'), ('1966', '1966'), ('1965', '1965'), ('1964', '1964'), ('1963', '1963'), ('1962', '1962'), ('1961', '1961'), ('1960', '1960'), ('1959', '1959'), ('1958', '1958'), ('1957', '1957'), ('1956', '1956'), ('1955', '1955'), ('1954', '1954'), ('1953', '1953'), ('1952', '1952'), ('1951', '1951'), ('1950', '1950'), ('1949', '1949'), ('1948', '1948'), ('1947', '1947'), ('1946', '1946'), ('1945', '1945'), ('1944', '1944'), ('1943', '1943'), ('1942', '1942'), ('1941', '1941'), ('1940', '1940'), ('1939', '1939'), ('1938', '1938'), ('1937', '1937'), ('1936', '1936'), ('1935', '1935'), ('1934', '1934'), ('1933', '1933'), ('1932', '1932'), ('1931', '1931'), ('1930', '1930'), ('1929', '1929'), ('1928', '1928'), ('1927', '1927'), ('1926', '1926'), ('1925', '1925'), ('1924', '1924'), ('1923', '1923'), ('1922', '1922'), ('1921', '1921'), ('1920', '1920'), ('1919', '1919'), ('1918', '1918'), ('1917', '1917'), ('1916', '1916'), ('1915', '1915'), ('1914', '1914'), ('1913', '1913'), ('1912', '1912'), ('1911', '1911'), ('1910', '1910'), ('1909', '1909'), ('1908', '1908'), ('1907', '1907'), ('1906', '1906'), ('1905', '1905'), ('1904', '1904'), ('1903', '1903'), ('1902', '1902'), ('1901', '1901'), ('1900', '1900')], default=None, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='alert',
            name='year_min',
            field=models.CharField(blank=True, choices=[(None, 'Desde'), ('2017', '2017'), ('2016', '2016'), ('2015', '2015'), ('2014', '2014'), ('2013', '2013'), ('2012', '2012'), ('2011', '2011'), ('2010', '2010'), ('2009', '2009'), ('2008', '2008'), ('2007', '2007'), ('2006', '2006'), ('2005', '2005'), ('2004', '2004'), ('2003', '2003'), ('2002', '2002'), ('2001', '2001'), ('2000', '2000'), ('1999', '1999'), ('1998', '1998'), ('1997', '1997'), ('1996', '1996'), ('1995', '1995'), ('1994', '1994'), ('1993', '1993'), ('1992', '1992'), ('1991', '1991'), ('1990', '1990'), ('1989', '1989'), ('1988', '1988'), ('1987', '1987'), ('1986', '1986'), ('1985', '1985'), ('1984', '1984'), ('1983', '1983'), ('1982', '1982'), ('1981', '1981'), ('1980', '1980'), ('1979', '1979'), ('1978', '1978'), ('1977', '1977'), ('1976', '1976'), ('1975', '1975'), ('1974', '1974'), ('1973', '1973'), ('1972', '1972'), ('1971', '1971'), ('1970', '1970'), ('1969', '1969'), ('1968', '1968'), ('1967', '1967'), ('1966', '1966'), ('1965', '1965'), ('1964', '1964'), ('1963', '1963'), ('1962', '1962'), ('1961', '1961'), ('1960', '1960'), ('1959', '1959'), ('1958', '1958'), ('1957', '1957'), ('1956', '1956'), ('1955', '1955'), ('1954', '1954'), ('1953', '1953'), ('1952', '1952'), ('1951', '1951'), ('1950', '1950'), ('1949', '1949'), ('1948', '1948'), ('1947', '1947'), ('1946', '1946'), ('1945', '1945'), ('1944', '1944'), ('1943', '1943'), ('1942', '1942'), ('1941', '1941'), ('1940', '1940'), ('1939', '1939'), ('1938', '1938'), ('1937', '1937'), ('1936', '1936'), ('1935', '1935'), ('1934', '1934'), ('1933', '1933'), ('1932', '1932'), ('1931', '1931'), ('1930', '1930'), ('1929', '1929'), ('1928', '1928'), ('1927', '1927'), ('1926', '1926'), ('1925', '1925'), ('1924', '1924'), ('1923', '1923'), ('1922', '1922'), ('1921', '1921'), ('1920', '1920'), ('1919', '1919'), ('1918', '1918'), ('1917', '1917'), ('1916', '1916'), ('1915', '1915'), ('1914', '1914'), ('1913', '1913'), ('1912', '1912'), ('1911', '1911'), ('1910', '1910'), ('1909', '1909'), ('1908', '1908'), ('1907', '1907'), ('1906', '1906'), ('1905', '1905'), ('1904', '1904'), ('1903', '1903'), ('1902', '1902'), ('1901', '1901'), ('1900', '1900')], default=None, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='external_id',
            field=models.CharField(default=datetime.datetime(2016, 6, 23, 23, 25, 36, 440524, tzinfo=utc), max_length=140),
            preserve_default=False,
        ),
    ]