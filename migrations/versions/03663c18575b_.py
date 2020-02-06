"""empty message

Revision ID: 03663c18575b
Revises: af72304ae017
Create Date: 2020-02-04 07:14:23.184567

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "03663c18575b"
down_revision = "af72304ae017"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("user", sa.Column("role", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("user", "role")
    # ### end Alembic commands ###
