class CreateUsers < ActiveRecord::Migration[5.0]
  def change
    create_table :users do |t|
      t.string :name
      t.string :city
      t.string :state

      t.timestamps
    end
  end
end
