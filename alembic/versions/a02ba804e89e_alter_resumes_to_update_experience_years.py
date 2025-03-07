"""Alter resumes to update experience_years

Revision ID: a02ba804e89e
Revises: bffc4eefa0e3
Create Date: 2024-07-28 17:49:10.160486

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a02ba804e89e"
down_revision: Union[str, None] = "bffc4eefa0e3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "resumes",
        "experience_years",
        existing_type=sa.INTEGER(),
        type_=sa.Float(),
        existing_nullable=True,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "resumes",
        "experience_years",
        existing_type=sa.Float(),
        type_=sa.INTEGER(),
        existing_nullable=True,
    )
    # ### end Alembic commands ###
