import click
import requests


API_URL = "http://localhost:8000"


@click.group()
def cli():
    pass


@cli.command()
@click.option("--x", required=True, type=float)
@click.option("--y", required=True, type=float)
def pow(x, y):
    r = requests.post(f"{API_URL}/pow", json={"x": x, "y": y})
    click.echo(f"Rezultat: {r.json()['result']}")


@cli.command()
@click.option("--n", required=True, type=int)
def fibonacci(n):
    r = requests.post(f"{API_URL}/fibonacci", json={"n": n})
    click.echo(f"Rezultat: {r.json()['result']}")


@cli.command()
@click.option("--n", required=True, type=int)
def factorial(n):
    r = requests.post(f"{API_URL}/factorial", json={"n": n})
    click.echo(f"Rezultat: {r.json()['result']}")


@cli.command()
@click.option("--user", prompt=True)
@click.option("--password", prompt=True, hide_input=True)
def clear_db(user, password):
    from requests.auth import HTTPBasicAuth
    r = requests.delete(
        f"{API_URL}/operations/clear",
        auth=HTTPBasicAuth(user, password)
    )
    if r.status_code == 200:
        click.echo("Baza de date a fost ștearsă.")
    else:
        click.echo(f"Eroare: {r.status_code} - {r.text}")


if __name__ == "__main__":
    cli()
