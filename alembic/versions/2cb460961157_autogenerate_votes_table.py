"""Autogenerate votes table

Revision ID: 2cb460961157
Revises: 1c68e2bdd878
Create Date: 2022-11-08 00:44:13.619516

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2cb460961157"
down_revision = "1c68e2bdd878"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "votes",
        sa.Column("post_id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["post_id"], ["posts.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("post_id", "user_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("votes")
    # ### end Alembic commands ###
